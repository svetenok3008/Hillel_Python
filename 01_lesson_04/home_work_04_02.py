a = [0, 7, 9, 12, -1, 100]

print("The first method:")
b = 0
i = 0
while i < (len(a)):
    b += a[i]
    i += 2
print(b * a[-1])

print("The second method:")
b = 0
for i in range(len(a)):
    if i % 2 == 0:
        b += a[i]
print(b * a[-1])
