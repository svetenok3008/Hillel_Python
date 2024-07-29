a = [0, 7, 9, 12, 75.2, 0, 100, 0, 2, 0, -1]
n = a.count(0)
for i in range(n):
    k = a.index(0)
    a.pop(k)
    a.append(0)
print(a)




