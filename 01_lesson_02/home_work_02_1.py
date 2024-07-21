num = int(input('Enter a 4-digit number: '))

# version 1:
print('solution 1:')
n_1 = num // 1000
print (n_1)
n_2 = (num - n_1*1000) // 100
print (n_2)
n_3 = (num - n_1*1000 - n_2*100) // 10
print (n_3)
n_4 = num % 10
print (n_4)

# version 2:
print('solution 2:')
n_1 = num // 1000
print (n_1)
n_2 = num % 1000 // 100
print (n_2)
n_3 = num % 100 // 10
print (n_3)
n_4 = num % 10
print (n_4)

# version 3:
print('solution 3:')
n_1_tuple = divmod(num,1000)
print (n_1_tuple[0])
n_2_tuple = divmod(n_1_tuple[1],100)
print (n_2_tuple[0])
n_3_tuple = divmod(n_2_tuple[1],10)
print (n_3_tuple[0])
print (n_3_tuple[1])