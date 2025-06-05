from turtle import *
from random import *
from time import *

t1 = Turtle()
t2 = Turtle()
lb = -300
rb = 300

t1.shape("turtle")
t2.shape("turtle")

t1.penup()
t1.goto(lb, 50)
t1.pendown()
t1.goto(lb, -50)

t1.penup()
t1.goto(rb, 50)
t1.pendown()
t1.goto(rb, -50)

t1.penup()
t2.penup()
t1.goto(lb, 40)
t2.goto(lb, -40)

while True:
    #pause = input('нажмите энтер чтобы продолжить')
    sleep(0.3)
    step1 = randint(1, 3)
    step2 = randint(1, 3)
    t1.fd(step1 * 10)
    t2.fd(step2 * 10)
    if t1.pos()[0] >= rb and t2.pos()[0] >= rb:
        print('ничья')
        t1.circle(20)
        t2.circle(20)
        break
    elif t1.pos()[0] >= rb:
        print('победила 1 черепашка')
        t1.circle(20)
        break
    elif t2.pos()[0] >= rb:
        t2.circle(20)
        print('победила 2 черепашка')
        break


done()
