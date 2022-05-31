import Crossfire

import CFTowerDefense as td

player = Crossfire.WhoIsActivator()
wrench = Crossfire.WhoAmI()
current_map = Crossfire.WhoIsActivator().Map
tile = td.player_objects(player, current_map)

Crossfire.SetReturnValue(1)

if tile and current_map.Path == '/darcap/darcap/circus/fz_tower_defense':
    result = False
    result |= td.replace_tower(current_map, tile, td.bulletwall)
    result |= td.replace_tower(current_map, tile, td.firewall, 40)
    result |= td.replace_tower(current_map, tile, td.lightningwall)
    if not result:
        player.Message("There is no tower in the direction you are facing to rotate.")
else:
    player.Message("Nothing happens here.")
