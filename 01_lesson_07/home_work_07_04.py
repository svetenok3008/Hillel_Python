def common_elements():
    multiple_of_3 = set()
    multiple_of_5 = set()
    for i in range(0, 101):
        if i % 3 == 0:
            multiple_of_3.add(i)
    for i in range(0, 101):
        if i % 5 == 0:
            multiple_of_5.add(i)
    return multiple_of_3.intersection(multiple_of_5)


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
