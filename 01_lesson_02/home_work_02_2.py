num = int(input('Enter a 5-digit number: '))

n_1 = num // 10000
n_2 = num % 10000 // 1000
n_3 = num % 1000 // 100
n_4 = num % 100 // 10
n_5 = num % 10

print(n_5*10000 + n_4*1000 + n_3*100 + n_2*10 + n_1)