# import numpy as np


ne_decoded = [-1, -1, -1]
level_list = []


with open('aboin.txt', 'r', encoding='utf-8') as f_txt:
    txt_lines = f_txt.readlines()
    for line in txt_lines:
        # print(line)
        ne_pos = line.find('NE = ')
        if ne_pos > 0:
            ne_str = line[ne_pos + 5:ne_pos + 13]
            ne_decoded[0] = ne_str.split('-')[0]
            ne_decoded[1] = ne_str.split('-')[1]
            ne_decoded[2] = ne_str.split('-')[2]
            #print(f'URA = {ne_decoded[0]}, level = {ne_decoded[1]}, user = {ne_decoded[2]}')

        sus_pos = line.find('+ SUS +')
        if sus_pos > 0:
            print(f'URA = {ne_decoded[0]}, level = {ne_decoded[1]}, user = {ne_decoded[2]}, status: SUS')
            n_user = int(ne_decoded[2])
            level_list.insert(n_user, 0)
            #sus_pos = -1
            #ne_pos = -1
            #ne_decoded = [-1, -1, -1]

    print(level_list)
    print(len(level_list))
