# trigger.py -- triggered connections from CFPython
#
# CFPython provides map.TriggerConnected() which triggers a connection once.
# However, in some circumstances, what you actually want is an "open" followed
# by a "close" after a delay (like 'arch trigger'). Many maps work around this
# with clever lightning walls, but this should not be necessary.
#
# Usage: In your script, in place of:
#   Crossfire.WhoAmI().Map.TriggerConnected(con, 1)
# Write:
#   import misc.trigger
#   misc.trigger.trigger(Crossfire.WhoAmI(), con)
#
# Bugs:
# - The timer created by CreateTimer does not survive across map resets, so
#   if the map happens to swap before the gate is un-triggered, the gate will
#   stay open.

import Crossfire

extra_debug = False

def flip_pol(pol):
    if pol != 0:
        return 0
    else:
        return 1

def trigger(ob, con, pol=1, delay=5):
    # add delayed close
    trigger_delay(ob, con, flip_pol(pol), delay)

    # now just open the gate
    if extra_debug:
        Crossfire.Log(Crossfire.LogDebug, "Triggering connection %d on %s" % (con, ob.Map.Path))
    ob.Map.TriggerConnected(con, pol)

def trigger_delay(ob, con, pol, delay):
    timer = Crossfire.CreateObjectByName("event_timer")
    timer.Title = "Python"
    timer.Name = "%d %d" % (con, pol)
    timer.Slaying = "/python/misc/trigger.py" # path to this script
    timer.InsertInto(ob)
    ob.CreateTimer(delay, 1) # in seconds

def do_delayed_trigger():
    ev = Crossfire.WhatIsEvent()
    if ev.Subtype == Crossfire.EventType.TIMER:
        parts = ev.Name.strip().split(" ")
        try:
            con = int(parts[0])
            pol = int(parts[1])
            if extra_debug:
                Crossfire.Log(Crossfire.LogDebug, "Un-triggering connection %d on %s" % (con, ev.Env.Map.Path))
            ev.Env.Map.TriggerConnected(con, pol)
        except Exception as e:
            Crossfire.Log(Crossfire.LogError, "Error parsing delayed trigger on %s: %s" % (ev.Env.Map.Path, e))
        ev.Remove()

do_delayed_trigger()
