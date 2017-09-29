# subtract list_2 from list_1
list_1 = [8, 5, 8]
list_2 = [5, 2, 5]
list_3 = [list_2[i] - list_1[i] for i in range(len(list_2))]
# for i in range(len(list_2)):
#     list_3.append(list_2[i] - list_1[i])

print(list_3)

# create a dict wtih 3 k-v pairs, loop and print each k-v pair, chk if a given val is in dict

char_1 = {'Name' : 'Luke', 'Power' : 'Force', 'Master' : 'Yoda'}
vals = []
for k, v in char_1:
    print(f'Key is {k} and value is {v}.')
    vals.append(v)
