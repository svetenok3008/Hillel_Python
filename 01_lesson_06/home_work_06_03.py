num_str = input('Input your number: ')
num = int(num_str)

while num > 9:
    num = 1
    for i in num_str:
        num = num * int(i)
    num_str = str(num)

print(num)
