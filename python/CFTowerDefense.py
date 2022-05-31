import Crossfire

bulletwall = [
    'lbulletwall_1',
    'lbulletwall_2',
    'lbulletwall_3',
    'lbulletwall_4',
    'lbulletwall_5',
    'lbulletwall_6',
    'lbulletwall_7',
    'lbulletwall_8',
]

lightningwall = [
    'lightningwall_1',
    'lightningwall_2',
    'lightningwall_3',
    'lightningwall_4',
    'lightningwall_5',
    'lightningwall_6',
    'lightningwall_7',
    'lightningwall_8',
]

firewall = [
    'firewall_1',
    'firewall_2',
    'firewall_3',
    'firewall_4',
    'firewall_5',
    'firewall_6',
    'firewall_7',
    'firewall_8',
]


def create_tower(player, current_map, tile, builder):
    """
    If a builder is dropped on a tower placement tile, a tower is built

    player: the player object
    current_map: the map object the player is in
    tile: all objects on a tile (a list of Crossfire objects)
    builder: the tower builder (a Crossfire object)

    Returns: True if a tower was built, False otherwise.
    """
    for ob in tile:
        if ob.Name == 'tower placement':
            # key/value: builder name/(arch name, spell level)
            builders = {
                'build large bullet tower': ('lbulletwall_1', 1),
                'build lightning tower': ('lightningwall_1', 1),
                'build fire tower': ('firewall_1', 40)
            }

            for name in builders:
                if name in builder.Name:
                    wall = Crossfire.CreateObjectByName(builders[name][0])
                    wall.Level = builders[name][1]

                    wall.Teleport(current_map, player.X, player.Y)
                    player.Teleport(current_map, player.X, player.Y+1)

                    builder.Quantity -= 1
                    return True
    return False


def destroy_tower(tile, towerlist):
    """
    If an object in tile exists in towerlist, the object is removed

    tile: all objects on a tile (a list of Crossfire objects)
    towerlist: bulletwall, firewall, or lightningwall

    Returns: True if a tower was destroyed, False otherwise.
    """
    for ob in tile:
        if ob.ArchName in towerlist:
            ob.Remove()
            return True
    return False


def replace_tower(current_map, tile, towerlist, level=0):
    """
    If an object in tile exists in towerlist, the object is replaced with the
    next direction in towerlist

    current_map: the map object the player is in
    tile: all objects on a tile (a list of Crossfire objects)
    towerlist: bulletwall, firewall, or lightningwall
    level: the spell level of the tower

    Returns: True if a tower was replaced, False otherwise.
    """
    for ob in tile:
        if ob.ArchName in towerlist:
            position = towerlist.index(ob.ArchName)
            x, y = ob.X, ob.Y

            if position == len(towerlist)-1:
                new_position = 0
            else:
                new_position = position+1

            ob.Remove()
            wall = Crossfire.CreateObjectByName(towerlist[new_position])
            wall.Teleport(current_map, x, y)

            # Add original rebalanced spell level for tower
            if level:
                wall.Level = level
            return True
    return False


def player_objects(player, current_map) -> list:
    """
    Returns all objects in the direction the player faces

    player: the player object
    current_map: the map object the player is in
    """
    # key/value: crossfire direction number/corresponding (x, y) coordinate
    directions = {
        Crossfire.Direction.NORTH: (player.X, player.Y-1),
        Crossfire.Direction.SOUTH: (player.X, player.Y+1),
        Crossfire.Direction.EAST: (player.X+1, player.Y),
        Crossfire.Direction.WEST: (player.X-1, player.Y),
        Crossfire.Direction.NORTHWEST: (player.X-1, player.Y-1),
        Crossfire.Direction.NORTHEAST: (player.X+1, player.Y-1),
        Crossfire.Direction.SOUTHWEST: (player.X-1, player.Y+1),
        Crossfire.Direction.SOUTHEAST: (player.X+1, player.Y+1)
    }
    x, y = directions[player.Facing]

    tile_ob = []
    ob = current_map.ObjectAt(x, y)
    while ob:
        tile_ob.append(ob)
        ob = ob.Above

    return tile_ob


def player_tile_objects(player, current_map) -> list:
    """
    Returns all objects in the tile the player is standing on

    player: the player object
    current_map: the map object the player is in
    """
    tile_ob = []
    ob = current_map.ObjectAt(player.X, player.Y)
    while ob:
        tile_ob.append(ob)
        ob = ob.Above

    return tile_ob
