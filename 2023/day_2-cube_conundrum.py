id_total = 0

for game in open('2023\data\\2.txt'):
    game = game.strip()
    game_id, hands = game.split(':')
    game_id = int(game_id.split()[-1])
    possible = True

    for hand in hands.split(';'):
        cube_count = {}
        for cube in hand.split(', '):
            count, colour = cube.split()

            if cube_count.get(colour):
                cube_count[colour] += int(count)
            else:
                cube_count[colour] = int(count)
        
        if cube_count.get('red'):
            if cube_count['red'] > 12:
                possible = False

        if cube_count.get('green'):
            if cube_count['green'] > 13:
                possible = False

        if cube_count.get('blue'):
            if cube_count['blue'] > 14:
                possible = False

    if possible:
        id_total += game_id

print(id_total)

id_total = 0

for game in open('2023\data\\2.txt'):
    game = game.strip()
    game_id, hands = game.split(':')
    game_id = int(game_id.split()[-1])

    cube_count = {}
    for hand in hands.split(';'):
        for cube in hand.split(', '):
            count, colour = cube.split()

            if cube_count.get(colour):
                if cube_count[colour] < int(count):
                    cube_count[colour] = int(count)
            else:
                cube_count[colour] = int(count)
        
    power = 1

    if cube_count.get('red'):
        power *= cube_count['red']

    if cube_count.get('green'):
        power *= cube_count['green']

    if cube_count.get('blue'):
        power *= cube_count['blue']
    print(power)
    id_total += power

print(id_total)
