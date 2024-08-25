def is_even(number):
    return True if int(str(number)[-1]) in range(0, 9, 2) else False


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('ok')
