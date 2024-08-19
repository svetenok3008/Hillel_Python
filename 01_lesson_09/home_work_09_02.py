def difference(*args: (int, float)) -> float:
    """The function finds the difference between max and min value of args.
    :args: any amount of int or float values,
    :return: float
    """
    if not args:
        args = [0]
    return round((max(args) - min(args)), 1)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
