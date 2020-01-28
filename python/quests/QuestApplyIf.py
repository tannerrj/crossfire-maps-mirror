# -*- coding: utf-8 -*-
# QuestApplyIf.py - A script to let an item be applied only if a quest
# reached a certain step
# Arguments are:
# - quest name
# - a list of steps, either single value (x) or range (x-y)
# If any matches, then the item can be applied, else it is not applied

import Crossfire

player = Crossfire.WhoIsActivator()
params = Crossfire.ScriptParameters()
args = params.split()

def can_apply(player):
    if type(player) == Crossfire.Player:
        questname = args[0]
        currentstep = player.QuestGetState(questname)

        for rule in args[1:]:
            if rule.find("-") == -1:
                startstep = int(rule)
                endstep = startstep
            else:
                startstep = int(rule.split("-")[0])
                endstep = int(rule.split("-")[1])
            if currentstep >= startstep and currentstep <= endstep:
                return True
    return False

if can_apply(player):
    Crossfire.SetReturnValue(1)
else:
    # forbid applying
    Crossfire.SetReturnValue(2)
    msg = Crossfire.WhoAmI().Message
    if type(player) == Crossfire.Player:
        if msg is not None:
            player.Message(msg.strip())
        else:
            player.Message("You cannot apply the %s now." % Crossfire.WhoAmI().Name)
