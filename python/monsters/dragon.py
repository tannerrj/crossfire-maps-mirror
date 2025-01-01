"""
dragon.py -- talking dragon that flies you places
Kevin Zheng 2024

This replaces the old dragon hangers, where every location that wanted a dragon
hanger needed to copy/paste a template map.

Usage: Put an event_say and event_apply handler that calls this script on a
dragon_exit.
"""

import math
import re

import Crossfire

world_map_path_matcher = r"/world/world_(\d\d\d)_(\d\d\d)";

activator = Crossfire.WhoIsActivator()
event = Crossfire.WhatIsEvent()
whoami = Crossfire.WhoAmI()

price_per_worldmap_tile = 5*50 # price per world map tile traveled, in money units (silver)
max_fare = 150*50 # maximum fare per trip, in money units (silver)

# All the fun places we can go! Tuple of map path and X, Y coordinate.
destinations = {
    'Port Joseph': ('/world/world_101_114', 16, 39),
    'Red Town': ('/pup_land/terminal', 10, 12),
    'Wolfsburg': ('/world/world_128_109', 35, 13),
    'Brest': ('/world/world_107_123', 32, 30),
    'Navar': ('/world/world_121_116', 37, 46),
    'Darcap': ('/world/world_116_102', 29, 37),
    'Stoneville': ('/world/world_103_127', 5, 15),
    'Scorn': ('/world/world_105_115', 5, 37),
    'Lake Country': ('/world/world_109_126', 16, 20),
    'Santo Dominion': ('/world/world_102_108', 17, 12),
#   'Nurnberg': ('/pup_land/nurnberg/city', 25, 15), # needs a passport check
}

dest_searchable = {} # searchable index of destinations along with a canonical name

for key, val in destinations.items():
    dest_searchable[key.upper()] = (key, val)

# Some maps aren't on the world map, so give them coordinate overrides so that
# they don't charge max price but still respect distance-based fares.
coord_override = {
    '/pup_land/terminal': (94, 115), # 50 platinum from Scorn
}

def search_destination(name):
    name = name.upper()
    if name in dest_searchable:
        return dest_searchable[name]
    else:
        return None

def world_map_coord(path):
    """Try to extract the coordinates from a world map path."""
    if path in coord_override:
        return coord_override[path]
    groups = re.match(world_map_path_matcher, path)
    if groups is not None:
        coords = groups.group(1, 2)
        cx, cy = int(coords[0]), int(coords[1])
        return cx, cy
    return None

def fare(dest):
    curr_coord = world_map_coord(whoami.Map.Path)
    dest_coord = world_map_coord(dest[0])
    if curr_coord is None or dest_coord is None:
        return max_fare
    else:
        return min(max_fare, dist_fare(curr_coord, dest_coord))

def dist_fare(start, end):
    dist = math.hypot(end[0] - start[0], end[1] - start[1])
    return math.ceil(dist * price_per_worldmap_tile)

# State for each player. Dict (player_name: str, state) where state is
# (destination: str, price: int).
state = Crossfire.GetPrivateDictionary()

def handle_say():
    msg = Crossfire.WhatIsMessage()
    text = msg.split()
    if text[0] == "what":
        whoami.Say("Dragon Express can whisk you to one of %d locations for a small fee. Travel faster today!" % len(destinations))
        return
    elif text[0] == "where":
        whoami.Say("We have %d exciting destinations: %s. Where would you like to go?" % (len(destinations), ", ".join(destinations.keys())))
        return
    elif text[0] == "yes" and activator.Name in state:
        dest_name = state[activator.Name][0]
        price = state[activator.Name][1]
        dest = destinations[dest_name]
        m = Crossfire.ReadyMap(dest[0])
        if not m:
            whoami.Say("Oops, it looks like the landing site there is not clear. Let's try to go somewhere else.")
        elif activator.PayAmount(price):
            activator.Message("You pay the %s %s" % (whoami.Name, Crossfire.CostStringFromValue(price)))
            activator.Message("You hop on the %s and it takes off. You enjoy a pleasant ride above the clouds before arriving at %s." % (whoami.Name, dest_name))
            activator.Teleport(m, dest[1], dest[2])
        else:
            whoami.Say("It doesn't look like you can afford this trip. Please come back when you can.")
        del(state[activator.Name])
        return

    dest = search_destination(msg)
    if dest is not None:
        dest_name = dest[0]
        dest = dest[1]
        price = fare(dest)
        whoami.Say("Alright, let's go to %s. That will cost %s. Is that okay?" % (dest_name, Crossfire.CostStringFromValue(price)))
        Crossfire.AddReply("yes", "Okay, let's go.")
        Crossfire.AddReply("no", "No thanks.")
        state[activator.Name] = (dest_name, price)
    else:
        whoami.Say("Welcome to Dragon Express. Where can I take you today?")
        Crossfire.AddReply("what", "What is Dragon Express?")
        Crossfire.AddReply("where", "Where can you take me?")

Crossfire.SetReturnValue(1)
if event.Subtype == Crossfire.EventType.SAY:
    handle_say()
else:
    activator.Say("Hello!")
