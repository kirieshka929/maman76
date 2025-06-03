for i in range(1, 101):
    if i % 10 == 1:
        print(i, 'манул')
    elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
        print(i, 'манула')
    elif i % 10 >= 5 and i % 10 <= 10 or i % 10 == 0 :
        print(i, 'манулов')