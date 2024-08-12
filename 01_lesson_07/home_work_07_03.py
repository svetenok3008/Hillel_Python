def second_index(text, some_str):
    item_ind = None
    first_ind = text.find(some_str)
    if first_ind != -1:
        if text.find(some_str, first_ind + 1) != -1:
            item_ind = text.index(some_str, first_ind + 1)
    return item_ind


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
