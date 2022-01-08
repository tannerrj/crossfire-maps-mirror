import Crossfire

import CFTowerDefense as td

player = Crossfire.WhoIsActivator()
wrench = Crossfire.WhoAmI()
current_map = Crossfire.WhoIsActivator().Map
tile = td.player_objects(player, current_map)

Crossfire.SetReturnValue(1)

if tile and current_map.Path == '/darcap/darcap/circus/fz_tower_defense':
    walls = td.bulletwall+td.firewall+td.lightningwall
    td.destroy_tower(tile, walls)
