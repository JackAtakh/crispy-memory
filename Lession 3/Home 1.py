#
# n=input('Выберите камень ножницы или бумага: ').lower()
# n1=input('Выберите камень ножницы или бумага: ').lower()
#
# if n=='камень' and n1=='бумага':
#     print(n1,'Победил')
# elif n1=='камень' and n=='бумага':
#     print(n,'Победил')
# elif n=='камень' and n1=='ножницы':
#     print(n,'Победил')
# elif n1=='камень' and n=='ножницы':
#     print(n1,'Победил')
# elif n=='ножницый' and n1=='бумага':
#     print(n,'Победил')
import random


s = input('Вы запустили игру Камень, ножницы, бумага,если хотите поиграть нажмите 1: ')

if s == '1':
    print('Если захотите закончить вводите +')
    print('Если захотите узнать счёт вводите t ')
    u_b= 0
    r = 0
    while True:
        user = input("Камень=1, ножницы=2 или бумага=3?: ")
        l = ['1', '2', '3']
        if user in l:
            r = random.choice(l)
            print(r)

            if r== '1' and user == 'н':
                r += 1
            elif r == '1' and user == 'б':
                u_b += 1
            elif r == '2' and user == 'к':
                u_b += 1
            elif r == '2' and user == 'б':
                r += 1
            elif r == '3' and user == 'н':
                u_b += 1
            elif r == '3' and user == 'к':
                r += 1
        elif user == 't':
            print('Ваши баллы ', u_b, '. Балы вашего соперника ', r, )
        elif user == '-':
            print('Ваши баллы - ', u_b, '. Балы вашего соперника ', r, )
            print('Конец игры! Заходите ещё!')
            break
        else:
            print('Вводите 1, 2 или 3')


if s== '-':
    print('Жаль')
else:
    print('Простите, я вас не понял')