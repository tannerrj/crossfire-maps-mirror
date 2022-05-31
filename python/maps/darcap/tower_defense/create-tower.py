import Crossfire

import CFTowerDefense as td

player = Crossfire.WhoIsActivator()
builder = Crossfire.WhoAmI()
current_map = Crossfire.WhoIsActivator().Map
tile = td.player_tile_objects(player, current_map)

Crossfire.SetReturnValue(1) # do not read the card normally

if tile and current_map.Path == '/darcap/darcap/circus/fz_tower_defense':
    if td.create_tower(player, current_map, tile, builder):
        player.Message("You build a tower.")
    else:
        player.Message("You must be standing on a tower placement square to build a tower.")
else:
    player.Message("Nothing happens here.")
