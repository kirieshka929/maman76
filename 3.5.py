a = [3, 4, 5, 2, 5, 3, 5, 3, 3, 2, 4]
c = 0
d = 0
for i in range(len(a)):
    if (a[i] - 1) % 2 == 0 or a[i] % 2 == 0 :
        c = c + a[i]
        d = d + 1
        # print('текущий индекс', i)
        # print('текущая массив', a[i])
print(c / d)
