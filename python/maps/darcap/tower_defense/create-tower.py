import Crossfire

import CFTowerDefense as td

player = Crossfire.WhoIsActivator()
builder = Crossfire.WhoAmI()
current_map = Crossfire.WhoIsActivator().Map
tile = td.player_tile_objects(player, current_map)

Crossfire.SetReturnValue(1)

if tile and current_map.Path == '/darcap/darcap/circus/fz_tower_defense':
    td.create_tower(player, current_map, tile, builder)
