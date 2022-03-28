#CFWorld.py
#A small module for checking where is bigworld an object is if it's in bigworld.
import math

import Crossfire

world_prefix = "/world/world_"
world_prefix_len = len(world_prefix)
world_len = len(world_prefix) + len('xxx_xxx')
world_sep = '_'
bigmapxsize = 50
bigmapysize = 50

#Return an x,y tuple of where in bigworld an object is. Return false if not in bigworld. In current bigworld, values range from 5000 to 6499.
def loc_from_ob(ob):
    cfmap = ob.Map
    if ((cfmap.Path.find(world_prefix) != 0) or (len(cfmap.Path) != world_len)):
        return False
    strloc = cfmap.Path[world_prefix_len:].split(world_sep)
    x = (int(strloc[0]) * bigmapxsize) + ob.X
    y = (int(strloc[1]) * bigmapysize) + ob.Y
    return (x, y)

def getdiff(loc1, loc2):
    return (loc1[0]-loc2[0], loc1[1]-loc2[1])

def getdir(v):
    x, y = v
    t = math.atan2(x, y)
    rt = round(t / (math.pi/4)) # between -4 and 4
    directions = ["north", "northwest", "west", "southwest", "south", "southeast", "east", "northeast"]
    dir_str = directions[(rt + 4)%8]
    return dir_str

#outputs in furlongs (outdoor tiles)
def getdist(loc):
    return int(math.sqrt((loc[0]*loc[0])+(loc[1]*loc[1])))
