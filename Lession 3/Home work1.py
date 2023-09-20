print('1-Изменит ел изсписка\n2-Удалит эл из списка\n3-добавить 1 эл')
n=['Hello','Jack','Vadim']
user = input('выберите между 1 2 и 3: ')
if user==str(1) and len(n)<=1:
    print(n)
    u=input('Какой эл вы хотите изменит : ')
    n.remove(u)
    print(n)
    i=input('На какой эл вы хотите изменить: ')
    n.append(i)
    print(n)
elif user==str(2) and len(n)==0:
    print('Список пустой')
elif user==str(2) and len(n)==1:
    print(n)
    user1=input('Какой эл вы хотите удалит : ')
    n.remove(user1)
    print(n)
elif user==str(3):
    user2=input('Какой эл вы хотите добавит: ')
    n.append(user2)
    print(n)






