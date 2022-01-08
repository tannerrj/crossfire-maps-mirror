import Crossfire

private_dict = Crossfire.GetPrivateDictionary()
value = Crossfire.ScriptParameters()
current_map = Crossfire.WhoAmI().Map

if value == 'reset':
    private_dict['death'] = 0
else:
    private_dict['death'] += 1

    # End of wave 1
    if private_dict['death'] == 120:
        current_map.TriggerConnected(999, 1)

    # End of wave 2
    elif private_dict['death'] == 240:
        current_map.TriggerConnected(1000, 1)
        private_dict['death'] = 0

# Crossfire.Log(Crossfire.LogError, f"{private_dict['death']}")
