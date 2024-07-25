list_1 = [56, 78, 20, -77, 0, 1, 'aa']
len_list = len(list_1)

if len_list == 0:
    new_list_1 = []
    new_list_2 = []
elif len_list % 2 == 1:
    new_list_1 = list_1[:len_list // 2 + 1]
    new_list_2 = list_1[len_list // 2 + 1:]
else:
    new_list_1 = list_1[:len_list // 2]
    new_list_2 = list_1[len_list // 2:]

new_list = [new_list_1, new_list_2]
print(new_list)
