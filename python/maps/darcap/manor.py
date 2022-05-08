# -*- coding: utf-8 -*-
# Script handling various things for Darcap Manor.
#
# It is used:
# - in the blue zone, to count how many kobolds are on the map
# - in the brown zone, to prevent Kaptel's death or trigger the opening of the exit
# - in the white zone, to check if the player knows how many of a certain jewel there are
# - for the potion, to explode walls in the treasure room
# - in the treasure room, to select the reward

import random
import Crossfire

def blue_count_kobolds():
    '''Count the number of kobolds on the map for the blue zone.'''
    map = Crossfire.WhoAmI().Map
    count = 0
    for x in range(map.Width):
        for y in range(map.Height):
            below = map.ObjectAt(x, y)
            while below:
                if below.Name == 'kobold' or below.Name == 'Second Chance kobold':
                    count = count + 1
                    break
                below = below.Above

    return count

def blue_check():
    '''Player triggered the lever, check if correct number of kobolds.'''

    if blue_count_kobolds() != 4:
        Crossfire.SetReturnValue(1)
        Crossfire.WhoIsActivator().Message('The level will only activate if there are exactly 4 kobolds on the map')
        return

def potion_check():
    """Handle the Darcap Manor's potion being thrown. Check if walls to destroy in the treasure room."""

    # note: duplication with /CFMove.py, should be factorised at some point
    dir_x = [ 0, 0, 1, 1, 1, 0, -1, -1, -1 ]
    dir_y = [ 0, -1, -1, 0, 1, 1, 1, 0, -1 ]

    env = Crossfire.WhoAmI().Env

    if env.Map.Path != '/darcap/darcap/manor.treasure':
        return

    x = env.X + dir_x[ env.Direction ]
    y = env.Y + dir_y[ env.Direction ]

    if y != 4 and y != 8 and y != 12:
        return

    if x != 4 and x != 5:
        return

    left = env.Map.Check('cwall_mural_1_1', (4, y))
    right = env.Map.Check('cwall_mural_1_2', (5, y))

    if left == None or right == None:
        # hu?
        return

    left.Remove()
    right.Remove()

    env.Map.CreateObject('rubble', 4, y)
    env.Map.CreateObject('rubble', 5, y)
    env.Map.CreateObject('explosion2', 4, y)
    env.Map.CreateObject('explosion2', 5, y)

    Crossfire.WhoAmI().Remove()

    env.Map.Print('The wall explodes!')

def kaptel_death():
    '''
    Handle Kaptel's death event. Depending on whether the player triggered the lever,
    either prevent death or trigger the opening of the exit.
    '''
    who = Crossfire.WhoAmI()

    floor = who.Map.ObjectAt(24, 1)
    while floor != None and floor.Above != None:
        floor = floor.Above

    if floor.Name == 'boulder':
        who.Say('AAAAAAAAAaaaaahhhhhhhhhhhhhh!!!!!!!!!')
        who.Map.TriggerConnected(11, 1)
        return

    who.Map.Print("%s roars and seems to regenerate!"%(Crossfire.WhoAmI().Name))
    who.HP = int(who.MaxHP / 2)
    Crossfire.SetReturnValue(1)

def challenge_correct_reply(count, msg):
    '''Check if the reply to the challenge is correct.'''
    if count == 0:
        return msg == '0' or msg == 'none'
    return count == int(msg)

def check_arch(map, x, y, arch):
    below = map.ObjectAt(x, y)
    while below:
        if below.ArchName == arch:
            return 1
        below = below.Above

    return 0

def white_challenge():
    '''
    Say handler for the final white challenge.
    Player must know how many jewel piles of a certain kind were on the map, else failure.
    '''

    msg = Crossfire.WhatIsMessage()
    ear = Crossfire.WhoAmI()
    status = ear.ReadKey('challenge')

    if status == 'done':
        ear.Say('You already replied!')
        return

    if status == '':
        if msg == 'ready':
            ear.WriteKey('challenge', 'ready', 1)
            ear.Say('To get the white key, reply to the following question:')

            archs = [ 'gem', 'amethyst', 'emerald', 'ruby', 'sapphire', 'pearl' ]
            names = [ 'diamonds', 'amethysts', 'emeralds', 'rubies', 'sapphires', 'pearls' ]
            choice = random.randint(0, 5)

            behind_windows = { (8, 2), (10, 7), (10, 9), (28, 18) }
            behind_grates = { (2, 23), (10, 7), (10, 9), (16, 21), (19, 26), (19, 28), (20, 26), (23, 7), (24, 1), (24, 6), (25, 7) }

            location = random.randint(1, 3)
            if location == 1:
                positions = behind_windows
                where = 'behind windows'
            elif location == 2:
                positions = behind_grates
                where = 'behind grates'
            else:
                positions = behind_windows.union(behind_grates)
                where = 'in this dungeon'

            count = 0
            for pos in positions:
                count += check_arch(ear.Map, pos[0], pos[1], archs[choice])

            ear.Say('How many piles of %s did you see %s?'%(names[choice],where))
            ear.Say('Reply with a number in digits please.')

            # keep reply in the ear, easier
            ear.WriteKey('reply', str(count), 1)
        return

    # check answer

    ear.WriteKey('challenge', 'done')

    count = int(ear.ReadKey('reply'))
    if challenge_correct_reply(count, msg):
        ear.Map.TriggerConnected(60, 1)
        ear.Say('Correct!')
    else:
        ear.Say('Sorry, that is not the correct reply. Please try again later.')

def claim_reward():
    '''Handle the player applying the lever to get her reward.'''
    rewards = { # Gate positions for the rewards
        'amethysts': [2, 15],
        'glowing_crystal': [2, 17],
        'potion': [3, 18],
        'townportal': [5, 18],
        'lunar_shield': [7, 18],
        'wizard_gloves': [10, 15],
        'black_dragon_mail': [10, 17],
    }
    chances = [ # Possible rewards, one is selected in the list so some items are repeated to make them more probably
        'amethysts',
        'amethysts',
        'amethysts',
        'amethysts',
        'glowing_crystal',
        'glowing_crystal',
        'glowing_crystal',
        'potion',
        'potion',
        'townportal',
        'townportal',
        'lunar_shield',
        'wizard_gloves',
        'black_dragon_mail',
    ]

    def swap_gate(item, delete = False):
        # lever.Map.Print('item = %d'%(item))
        x = rewards[chances[item]][0]
        y = rewards[chances[item]][1]
        gate = lever.Map.ObjectAt(x, y).Above.Above
        replace = ''
        glow = 0
        if gate.ArchName == 'grate_closed_1':
            replace = 'igate_closed_1'
        elif gate.ArchName == 'grate_closed_2':
            replace = 'igate_closed_2'
        elif gate.ArchName == 'igate_closed_1':
            replace = 'grate_closed_1'
            glow = 5
        elif gate.ArchName == 'igate_closed_2':
            replace = 'grate_closed_2'
            glow = 5
        else:
            # lever.Map.Print('found %s'%(gate.ArchName))
            return
        # lever.Map.Print('%d %d %s => %s'%(x, y, gate.ArchName, replace))
        gate.Remove()
        if delete:
            return
        ob = lever.Map.CreateObject(replace, x, y)
        if glow != 0:
            ob.GlowRadius = glow


    Crossfire.SetReturnValue(1)
    lever = Crossfire.WhoAmI()
    event = Crossfire.WhatIsEvent()
    status = lever.ReadKey('status')
    if event.Subtype == Crossfire.EventType.APPLY:
        if status == '':
            lever.Map.Print('And now you shall get your reward!')
            lever.WriteKey('status', 'start', 1)
            lever.WriteKey('reward', str(random.randint(0, len(chances))), 1)
            lever.WriteKey('left', str(random.randint(1, 3) + random.randint(1, 3) + random.randint(1, 3)), 1)
            lever.WriteKey('current', '-1', 1)
            lever.CreateTimer(1 + random.randint(1, 3), 2)
        return
    elif event.Subtype == Crossfire.EventType.TIMER:
        if lever.Map.Darkness < 5:
            lever.Map.ChangeLight(1)
            lever.CreateTimer(1 + random.randint(1, 3), 2)
            return

        left = int(lever.ReadKey('left'))
        current = int(lever.ReadKey('current'))
        if left == 0:
            lever.Map.Print("Yes! Congratulations!")
            while lever.Map.Darkness > 0:
                lever.Map.ChangeLight(-1)
            swap_gate(current, True)
            
        else:
            if current != -1:
                lever.Map.Print('No!')
                # lever.Map.Print('restoring')
                swap_gate(current)
                lever.WriteKey('current', '-1', 1)
                lever.CreateTimer(1 + random.randint(1, 3), 2)
                return

            left -= 1
            lever.WriteKey('left', str(left), 1)
            
            current = random.randint(0, len(chances) - 1)
            swap_gate(current)
            lever.WriteKey('current', str(current), 1)
            lever.CreateTimer(1 + random.randint(1, 2), 1)
            lever.Map.Print('Will it be this reward?')

def politos():
    '''Handle Politos's dialog in the entrance.'''
    msg = Crossfire.WhatIsMessage()
    politos = Crossfire.WhoAmI()
    pl = Crossfire.WhoIsActivator()
    status = politos.ReadKey('opened')

    if msg == 'potion':
        politos.Say("This potion will replace any of the three keys, but you have to figure out how to use it yourself.")
    elif msg == 'yes' and status == '':
        politos.Say('Ok, good luck')
        politos.Map.TriggerConnected(1, 1)
        politos.WriteKey('opened', 'yes', 1)
    elif status != '':
        politos.Say('Feel free to go try get the keys now.')
    else:
        politos.Say(
            'Welcome to Darcap Manor. Here you can attempt to find some exclusive rewards!\n'
            'To get a treasure from upstairs, you need to find three keys: blue, white, brown.\n'
            'You can get one from each of the corners of this room, provided you are strong or smart enough, of course.\n'
            # 'If you go downstairs, you can attempt to get a random key, but you must be lucky.\n\n'
            'So do you wish to enter?'
        )
    Crossfire.SetReturnValue(1)

params = Crossfire.ScriptParameters()

if params == 'blue':
    blue_check()
elif params == 'potion':
    potion_check()
elif params == 'kaptel':
    kaptel_death()
elif params == 'white':
    white_challenge()
elif params == 'reward':
    claim_reward()
elif params == 'politos':
    politos()
