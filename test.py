

list = []

list += ['1', 'null', 'null']

for i, target_list in enumerate(list):

    if target_list == 'null':
        list[i] = None


print(list)
