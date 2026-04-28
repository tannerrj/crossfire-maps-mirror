import Crossfire

if Crossfire.WhoAmI().DungeonMaster:
    args = Crossfire.ScriptParameters()
    try:
        num = int(args)
        Crossfire.WhoAmI().Map.TriggerConnected(num, 1)
        Crossfire.WhoAmI().Message("Triggered connection %d." % num)
    except (ValueError, TypeError):
        Crossfire.WhoAmI().Message("A numeric argument is required.")
    except ReferenceError:
        Crossfire.WhoAmI().Message("Connection %d does not exist on this map." % num)
else:
    Crossfire.WhoAmI().Message("Only dungeon masters may use this command.")
