from turtle import *
bgcolor('pink')
speed(50)

def square(side):
    for i in range(5):
        fd(side)
        forward(200)
        right(144)

for i in range(1, 200, 8):
     i = square(i + 10)

done()