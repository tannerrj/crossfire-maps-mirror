import Crossfire
import CFWorld

scorn_loc = (5272, 5786)
navar_loc = (6112, 5850)

Crossfire.SetReturnValue( 1 )

#outputs in miles
def getuserdist(dist):
    return (int(dist/8.0+0.5))

def gettext(loc1, loc2, name):
    diff = CFWorld.getdiff(loc2, loc1)
    loc_raw_dist = CFWorld.getdist(diff)
    loc_dist = getuserdist(loc_raw_dist)
    loc_dir = CFWorld.getdir(diff)
    if (abs(loc_dist) > 5):
        loc_distmsg = "A "+name+" arrow flashes "+str(loc_dist)+" times"
    else:
        loc_distmsg = "A "+name+" arrow glows steady"
    if (loc_raw_dist):
        loc_distmsg += ", pointing to the "+loc_dir+"."
    else:
        loc_distmsg += ", spinning in one place."
    return loc_distmsg

pl = Crossfire.WhoIsActivator()
me = Crossfire.WhoAmI()

location = CFWorld.loc_from_ob(pl)
if (location):
    scorntxt = gettext(location, scorn_loc, "red")
    navartxt = gettext(location, navar_loc, "blue")
    pl.Write(scorntxt+" "+navartxt)
else:
    pl.Write("The amulet doesn't seem to work here.")
