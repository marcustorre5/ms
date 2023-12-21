from random import randint
from time import sleep

while True:

    print('MS')
    s = input(str('[1] m1 - por sequencia\n[2] m2 - maior cores predominantes\n[3] m3 - numeros proximos da moda\n[0] SAIR\n'))

    if s == '1':
        def m1():
            n1 = randint(1, 10)
            n2 = randint(11, 20)
            n3 = randint(21, 40)
            n4 = randint(21, 40)
            n5 = randint(41, 50)
            n6 = randint(51, 60)
            print(n1, n2, n3, n4, n5, n6)


        m1()

    if s == '2':
        def m2():
            n1 = randint(1, 10)
            n2 = randint(11, 20)
            n3 = randint(11, 30)
            n4 = randint(21, 40)
            n5 = randint(41, 60)
            n6 = randint(51, 60)
            print(n1, n2, n3, n4, n5, n6)


        m2()

    if s == '3':
        def m3():
            n1 = randint(3, 9)
            n2 = randint(12, 18)
            n3 = randint(23, 37)
            n4 = randint(26, 40)
            n5 = randint(38, 50)
            n6 = randint(51, 60)
            print(n1, n2, n3, n4, n5, n6)


        m3()

    print('=========\n')
    sleep(2)

    if s == '0':
        break