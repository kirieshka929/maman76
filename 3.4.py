from random import *
a = randint(1, 10)
l = 3
print()
while l > 0:
    print('осталось жизней', l)
    print('какое число загадано?')
    u = int(input())
    if u == a:
        print('Победа')
        break
    elif a > u:
        print('загаданное число больше')
    else:
        print('загаданное число меньше')
    l -= 1
print('Было загадано число', a)
