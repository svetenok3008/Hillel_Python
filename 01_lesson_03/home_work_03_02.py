list_1 = [1, 9, 89, 54, -1, 'smth']
list_2 = list_1
len_list = len(list_1)

if len_list > 1:
    element = list_2.pop()
    list_2.insert(0, element)
    print(list_2)

if list_2 >= list_1:
    print("All is correct! Congratulations!")
else:
    print("Something is wrong. Check it out.")
