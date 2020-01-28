# Script for the roll-o-matic.
# Idea courtesy Alex Schultz.
#
# Copyright 2007 Nicolas Weeger
# Released as GPL
#
# This script makes its item move following tiles, in direction specified by a player

"""
Using this script:

1. Create a transport object in the map editor. Ensure that its type is actually TRANSPORT.

2. Add Python events that trigger this script. Transports require at least two events:

   - event_time, which periodically calls this script to move the transport along

   - event_apply and/or event_say, to start and stop the transport

   In practice, each event has fields:

    title Python
    slaying /python/items/roll-o-matic.py

   Optionally, add:

    name ship_mode

   Which makes roll-o-matic work for ships.
"""

import Crossfire

key_direction = 'rom_dir'
key_follow = 'rom_follow'

dir_x = [ 0, 0, 1, 1, 1, 0, -1, -1, -1 ]
dir_y = [ 0, -1, -1, 0, 1, 1, 1, 0, -1 ]

ship_mode = False

def is_floor(ob):
    if ship_mode:
        return ob.ArchName in {'sea_route', 'sea_route_2', 'sea_route_3', 'sea_route_4'}
    else:
        return ob.Floor == 1

def find_floor(x, y):
    """Find all objects satisfying is_floor() at the given location."""
    obj = me.Map.ObjectAt(x, y)
    while obj != None:
        if is_floor(obj):
            yield obj
        obj = obj.Above

def find_player():
    obj = me.Map.ObjectAt(me.X, me.Y)
    while obj != None:
        if obj.Type == Crossfire.Type.PLAYER:
            return obj
        obj = obj.Above
    return None

def has_floor(x, y, name):
    """Check whether one floor at the given location matches the given 'name'."""
    for ob in find_floor(x, y):
        if ob.Name == name:
            return True
    return False

def abs_dir(d):
    while d < 1:
        d = d + 8
    while d > 8:
        d = d - 8
    return d

def stop():
    me.WriteKey(key_direction, '', 1)
    me.WriteKey(key_follow, '', 1)
    me.Map.Print('The %s stops moving.'%me.Name)

def try_move(check_directions, want_dir):
    floor = me.ReadKey(key_follow)
    x = me.X
    y = me.Y
    done = False
    for check in check_directions:
        d = abs_dir(want_dir + check)
        if has_floor(x + dir_x[d], y + dir_y[d], floor):
            # Next time, move in the direction we last moved in.
            # This heuristic helps follow the roads better.
            me.WriteKey(key_direction, str(d))
            if me.Move(d) == 0:
                continue

            if pl != None:
                pl.Move(d)
            done = True
            break

    if not done:
        stop()

def do_shipwreck(me):
    stop()

def handle_move():
    want_dir = me.ReadKey(key_direction)
    floor = me.ReadKey(key_follow)
    if want_dir == '' or floor == '':
        return
#   me.Map.Print('roll')
    pl = find_player()
    want_dir = int(want_dir)
    if ship_mode:
        # For ship routes, check all candidate directions except the opposite-direction one.
        check_directions = [0, 1, -1, 2, -2, 3, -3]

        curr_tile = me.Map.ObjectAt(me.X, me.Y)
        while curr_tile != None:
            if curr_tile.Name == 'shipwreck':
                do_shipwreck(me)
                return
            curr_tile = curr_tile.Above
    else:
        # For roads, only check the routes that make progress in the right direction.
        check_directions = [0, 1, -1]
    try_move(check_directions, want_dir)

def start_move(want_dir):
    floors = list(find_floor(me.X, me.Y))
    if len(floors) < 1:
        return
    floor = floors[0].Name

    if me.ReadKey(key_direction) == '':
        me.Map.Print('The %s starts moving!' % me.Name)

    me.WriteKey(key_direction, str(want_dir), 1)
    me.WriteKey(key_follow, floor, 1)

def handle_say():
    msg = Crossfire.WhatIsMessage()
    if msg == 'stop':
        if me.ReadKey(key_direction) != '':
            stop()
        return

    want_dir = -1

    for d in Crossfire.DirectionName.keys():
        if msg == Crossfire.DirectionName[d].lower():
            want_dir = d
            break

    if want_dir == -1:
        return

    start_move(want_dir)

def handle_apply():
    if pl.Transport != None:
        # Stop if already moving.
        stop()
    else:
        # When applied, we don't know initial direction. Try to find one.
        start_move(0)
        try_move([0, 1, 2, 3, 4, 5, 6, 7], 0)
    Crossfire.SetReturnValue(0)

def do_handle():
    if me.Map == None:
        return

    if "ship_mode" in params:
        global ship_mode
        ship_mode = True

    Crossfire.SetReturnValue(1)

    if evt.Subtype == Crossfire.EventType.SAY:
        handle_say()
    elif evt.Subtype == Crossfire.EventType.APPLY:
        handle_apply()
    elif evt.Subtype == Crossfire.EventType.TIME:
        handle_move()


evt = Crossfire.WhatIsEvent()
me = Crossfire.WhoAmI()
pl = Crossfire.WhoIsActivator()
params = Crossfire.ScriptParameters()

do_handle()
