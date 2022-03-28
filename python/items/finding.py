# finding.py -- apply event for amulets of finding
#
# These pieces of jewelry help players remember locations on the world map.
# Players can bind an amulet at any location on the world map. Applying a bound
# amulet shows players a message indicating which direction they should travel
# to return to the bound location.
#
# The bound location is stored in the key-value pair "finding_location", which
# contains a 2-tuple of global coordinates from the CFWorld module.
import Crossfire
import CFWorld

location_key = 'finding_location'
world_size = 50

def indefinite(ob):
    """Append 'a' or 'an' to the given object's name."""
    name = ob.QueryName()
    if name[0].lower() in {'a', 'e', 'i', 'o'}:
        article = "an"
    else:
        article = "a"
    return article + " " + name

def auto_identify(ob, pl):
    """Identify the object if it hasn't already."""
    if not ob.Identified:
        ob.Identified = True
        pl.Message("This is %s!" % indefinite(ob))

def loc_to_str(l):
    return ",".join(map(str, l))

def str_to_loc(s):
    return list(map(int, s.split(",")))

def describe_vec(v):
    dist = CFWorld.getdist(v)
    if dist < 1:
        return "here"
    if dist <= world_size:
        modifier = "strongly"
    elif dist <= 5*world_size:
        modifier = "moderately"
    else:
        modifier = "lightly"
    return modifier + " " + CFWorld.getdir(v)

def on_apply():
    whoami = Crossfire.WhoAmI()
    player = Crossfire.WhoIsActivator()

    Crossfire.SetReturnValue(1) # do not allow players to wear this
    auto_identify(whoami, player)

    if whoami.Env == player:
        # applied in inventory
        current_location = CFWorld.loc_from_ob(player)
    else:
        # applied on the floor
        current_location = CFWorld.loc_from_ob(whoami)

    if current_location == False:
        # can only be used on the world map
        player.Message("The %s rattles for a moment, then stops." % whoami.QueryName())
        return

    if whoami.Env == player:
        # applied in inventory
        stored_str = whoami.ReadKey(location_key)
        if stored_str == "":
            # no location bound
            player.Message("The %s vibrates for a moment, then stops." % whoami.QueryName())
            return
        stored_location = str_to_loc(stored_str)
        delta = CFWorld.getdiff(stored_location, current_location)
        player.Message("The %s tugs you %s." % (whoami.QueryName(), describe_vec(delta)))
    else:
        # applied on the floor
        whoami.WriteKey(location_key, loc_to_str(current_location), 1)
        player.Message("The %s glows blue." % whoami.QueryName())

on_apply()
