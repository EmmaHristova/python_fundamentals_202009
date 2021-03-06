# 07-03. OBJECTS AND CLASSES [More Exercises]
# 05. Dragon Army

n = int(input())

dragons = {}

for i in range(n):
    dragon_type, dragon_name, damage, health, armor = input().split(' ')

    key = dragon_type, dragon_name

    if damage == 'null':
        damage = 45
    else:
        damage = int(damage)

    if health == 'null':
        health = 250
    else:
        health = int(health)

    if armor == 'null':
        armor = 10
    else:
        armor = int(armor)

    dragons[key] = damage, health, armor

dragon_types = {}

for dragon, stats in dragons.items():
    if dragon[0] not in dragon_types:
        dragon_types[dragon[0]] = [0, 0, 0, 0]
    dragon_types[dragon[0]][0] += stats[0]
    dragon_types[dragon[0]][1] += stats[1]
    dragon_types[dragon[0]][2] += stats[2]
    dragon_types[dragon[0]][3] += 1

dragons = dict(sorted(dragons.items(), key=lambda x: (x[0][1])))

for dragon_type in dragon_types:
    divider = dragon_types[dragon_type][3]
    dragon_types[dragon_type] = [stat / divider for stat in dragon_types[dragon_type]]

for dragon_type, stats_type in dragon_types.items():
    print(f'{dragon_type}::({stats_type[0]:.2f}/{stats_type[1]:.2f}/{stats_type[2]:.2f})')
    for dragon, stats in dragons.items():
        if dragon[0] == dragon_type:
            print(f'-{dragon[1]} -> damage: {stats[0]}, health: {stats[1]}, armor: {stats[2]}')
