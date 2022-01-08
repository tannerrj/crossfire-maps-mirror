import Crossfire

player = Crossfire.WhoIsActivator()
pedestal = Crossfire.WhoAmI()

# key/value: direction player is facing/direction player should be moved
directions = {
    Crossfire.Direction.NORTH: Crossfire.Direction.SOUTH,
    Crossfire.Direction.SOUTH: Crossfire.Direction.NORTH,
    Crossfire.Direction.EAST: Crossfire.Direction.WEST,
    Crossfire.Direction.WEST: Crossfire.Direction.EAST,
    Crossfire.Direction.NORTHWEST: Crossfire.Direction.SOUTHEAST,
    Crossfire.Direction.NORTHEAST: Crossfire.Direction.SOUTHWEST,
    Crossfire.Direction.SOUTHWEST: Crossfire.Direction.NORTHEAST,
    Crossfire.Direction.SOUTHEAST: Crossfire.Direction.NORTHWEST
}

if player and player.Facing:
    player.Move(directions[player.Facing])
