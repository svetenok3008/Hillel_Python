def find_unique_value(some_list):
    for i in range(len(some_list) + 1):
        if some_list.count(some_list[i]) == 1:
            item = some_list[i]
            break
    return item


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
