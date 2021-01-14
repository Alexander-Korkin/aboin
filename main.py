# import numpy as np
from sys import argv

ne_decoded = [-1, -1, -1]
level_list = []
ne_list = [[], [], [], []]

if (len(argv)) < 2:
    exit('No file name')
script_name, file_name = argv

with open(file_name, 'r', encoding='utf-8') as f_txt:
    txt_lines = f_txt.readlines()
    for line in txt_lines:
        # print(line)
        ne_pos = line.find('NE = ')
        if ne_pos > 0:
            ne_str = line[ne_pos + 5:ne_pos + 13]
            ne_decoded[0] = ne_str.split('-')[0]
            ne_decoded[1] = ne_str.split('-')[1]
            ne_decoded[2] = ne_str.split('-')[2]
            # print(f'URA = {ne_decoded[0]}, level = {ne_decoded[1]}, user = {ne_decoded[2]}')

        sus_pos = line.find('+ SUS +')
        ty_pos = line.find('TY = ')
        if sus_pos > 0:
            # print(f'URA = {ne_decoded[0]}, level = {ne_decoded[1]}, user = {ne_decoded[2]}, status: SUS')
            n_user = int(ne_decoded[2])
            level_list.insert(n_user, 0)
            ne_list[0].insert(n_user, 0)
            ne_list[1].insert(n_user, ne_decoded[1])
            ne_list[2].insert(n_user, ne_decoded[2])
            ne_list[3].insert(n_user, ne_decoded[0])
            # sus_pos = -1
            # ne_pos = -1
            # ne_decoded = [-1, -1, -1]

        if (ty_pos >= 0) and (sus_pos == -1):
            # print(f'URA = {ne_decoded[0]}, level = {ne_decoded[1]}, user = {ne_decoded[2]}')
            n_user = int(ne_decoded[2])
            level_list.insert(n_user, 1)
            ne_list[0].insert(n_user, 1)
            ne_list[1].insert(n_user, ne_decoded[1])
            ne_list[2].insert(n_user, ne_decoded[2])
            ne_list[3].insert(n_user, ne_decoded[0])

    # print(level_list)
    # print(len(level_list))

res = ''
unit = ''
for i in range(len(level_list)):
    ne = f'{ne_list[3][i]}-{ne_list[1][i]}-{ne_list[2][i]} '
    if (len(unit) == 0) or (unit[-1] == '\n'):
        res += ne

    unit = str(level_list[i]) + '\n' if (i + 1) % 8 == 0 else str(level_list[i])

    if unit[-1] == '\n':
        status_eao = res[-8:] + unit[-2]
        status_eao = status_eao.replace(' ', '')
        if status_eao.count('0') == 8:
            unit = unit[-2] + ' No users\n'

        # print(prod)
        # print('u='+res[-8:]+unit[-2])

    res += unit

print(res)
"""print(ne_list[0])  # status
print(ne_list[2])  # ne user
print(ne_list[1])  # ne level
print(ne_list[3])  # ne ura"""

# input('Press Enter...')
