"""
This implements a custom trap that is put under doors in guilds to deal with
tailgaters (people without access who follow people with access through doors).

This used to do some weird cursing, but it's modern times now so this just
sends people to Scorn's jail.
"""

import Crossfire
from CFGuildClearance import CheckClearance

activator = Crossfire.WhoIsActivator()

Crossfire.SetReturnValue(1) # don't run the actual trap

Params = Crossfire.ScriptParameters().split()
ActionRequired = Params[2] # formerly A for arrest and D for curse, no longer used (always A)

if activator is None:
    pass
elif activator.Type != Crossfire.Type.PLAYER:
    pass
elif CheckClearance(Params, activator):
    pass
else:
    activator.Teleport(Crossfire.ReadyMap('/scorn/misc/jail'), 15, 1) # 15 minute sentence
