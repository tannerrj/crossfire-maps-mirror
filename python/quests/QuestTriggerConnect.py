# -*- coding: utf-8 -*-
# QuestTriggerConnect.py - A generic script to trigger connections based on Quest progress
#
# Copyright (C) 2010 The Crossfire Development Team
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
#
# This script is intended to be bound to event objects in order to conditionally trigger
# connections based on the status of a quest, used correctly it can reduce the need for
# markers to use checkinvs on.
# Usage: /python/quests/QuestTriggerConnect.py QUEST STATE CONNECTION [EDGE]
#  QUEST - quest identifier string
#  STATE - stages to trigger on
#  CONNECTION - connection number
#  EDGE - optional trigger edge, 1 (release) by default

import Crossfire

def trigger_connected(conn, state, player):
    if state == 0:
        name = "push"
    else:
        name = "release"
    Crossfire.Log(Crossfire.LogDebug, "QuestTriggerConnect.py: triggering connection number %d (%s)" % (conn, name))
    Crossfire.WhoAmI().Map.TriggerConnected(conn, state, player)

def trigger():
    player = Crossfire.WhoIsActivator()
    params = Crossfire.ScriptParameters()
    args = params.split()
    edge = 1 # transition type, 0 for push, 1 for release
    if len(args) < 3:
        raise IndexError("QuestTriggerConnect used with incorrect number of arguments")
    if len(args) >= 4:
        edge = int(args[3])
    conn = int(args[2])
    if type(player) != Crossfire.Player:
        return
    questname = args[0]
    currentstep = player.QuestGetState(questname)
    condition = args[1]
    if condition.find("-") == -1:
        startstep = int(condition)
        endstep = startstep
    else:
        startstep = int(condition.split("-")[0])
        endstep= int(condition.split("-")[1])
    if currentstep >= startstep and currentstep <= endstep:
        trigger_connected(conn, edge, player)

trigger()
