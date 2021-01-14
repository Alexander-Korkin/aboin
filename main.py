# import numpy as np
from sys import argv

ne_decoded = [-1, -1, -1]
# level_list = []
ne_list = [[], [], [], []]

if (len(argv)) < 2:
    exit('No file name')
script_name, file_name = argv


def user_to_ag(level, user):
    if int(user) < 64:
        ag_user = int(user) // 8 + 2
    else:
        ag_user = int(user) // 8 + 6

    if int(level) < 2:
        ag_level = int(level) + 1
    else:
        ag_level = int(level) + 2
    return str(f'{ag_level}-{ag_user}')


with open(file_name, 'r', encoding='utf-8') as f_txt:
    txt_lines = f_txt.readlines()
    for line in txt_lines:
        # print(line)
        ne_pos = line.find('NE = ')
        if ne_pos > 0:
            # print(line)
            ne_str = line[ne_pos + 5:ne_pos + 13]
            if ne_str[-1] == '\n':
                ne_str = ne_str[0:len(ne_str) - 1]
            ne_decoded[0] = ne_str.split('-')[0]  # ura
            ne_decoded[1] = ne_str.split('-')[1]  # level
            ne_decoded[2] = ne_str.split('-')[2]  # user
            # print(f'URA = {ne_decoded[0]}, level = {ne_decoded[1]}, user = {ne_decoded[2]}')

        sus_pos = line.find('+ SUS +')
        ty_pos = line.find('TY = ')
        if sus_pos > 0 or line.find('MAR = ') >= 0:
            # print(f'URA = {ne_decoded[0]}, level = {ne_decoded[1]}, user = {ne_decoded[2]}, status: SUS')
            n_user = int(ne_decoded[2])
            # level_list.insert(n_user, 0)
            ne_list[0].append(0)
            ne_list[1].append(ne_decoded[1])
            ne_list[2].append(ne_decoded[2])
            ne_list[3].append(ne_decoded[0])
            # ne_list[0].insert(n_user, 0)
            # ne_list[1].insert(n_user, ne_decoded[1])
            # ne_list[2].insert(n_user, ne_decoded[2])
            # ne_list[3].insert(n_user, ne_decoded[0])
            # sus_pos = -1
            # ne_pos = -1
            # ne_decoded = [-1, -1, -1]

        if (ty_pos >= 0) and (sus_pos == -1):
            # print(f'URA = {ne_decoded[0]}, level = {ne_decoded[1]}, user = {ne_decoded[2]}')
            n_user = int(ne_decoded[2])
            # level_list.insert(n_user, 1)
            ne_list[0].append(1)
            ne_list[1].append(ne_decoded[1])
            ne_list[2].append(ne_decoded[2])
            ne_list[3].append(ne_decoded[0])
            # ne_list[0].insert(n_user, 1)
            # ne_list[1].insert(n_user, ne_decoded[1])    # level
            # ne_list[2].insert(n_user, ne_decoded[2])    # user
            # ne_list[3].insert(n_user, ne_decoded[0])    # ura

    # print(level_list)
    # print(len(level_list))

res = ''
unit = ''
emptys = 'Empty boards:\n'
#empty_board = ''
for i in range(len(ne_list[0])):
    ne = f'{ne_list[3][i]}-{ne_list[1][i]}-{ne_list[2][i]} '
    if (len(unit) == 0) or (unit[-1] == '\n'):
        res += ne

    unit = str(ne_list[0][i]) + '\n' if (i + 1) % 8 == 0 else str(ne_list[0][i])

    if unit[-1] == '\n':
        status_eao = res[-8:] + unit[-2]
        status_eao = status_eao.replace(' ', '')
        if status_eao.count('0') == 8:
            ag = user_to_ag(ne_list[1][i], ne_list[2][i])
            unit = unit[-2] + f' No users, AG={ag}\n'
            empty_board = f'NE={ne_list[3][i]}-{ne_list[1][i]}-{int(ne_list[2][i])-7}<{ne_list[2][i]}{chr(9)}AG={ag}\n'
            emptys += empty_board
    res += unit


#print(res)
print(emptys)

"""for i in range(len(ne_list[0])):
    print(f'{ne_list[3][i]}-{ne_list[1][i]}-{ne_list[2][i]}: {ne_list[0][i]}')"""

"""print(ne_list[0])  # status
print(ne_list[2])  # ne user
print(ne_list[1])  # ne level
print(ne_list[3])  # ne ura"""

# input('Press Enter...')
