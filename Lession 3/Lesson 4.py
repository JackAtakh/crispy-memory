# name=['Pasha']
# for item in name:
#     print(item[0])
# my_list=(6,'a','2')


# for p in my_list:
#     print(p)
# # print(f'всЕГО {len(my_list)} ')


# my_t=(6,4,'2')
# for i in range(1,100):
#     print(my_t)

# words=['adopt','bake','beam','confide','grill','wave']
# past_t=[]
# for word in words:
#     if word[-1]!='e':
#         past_t.append(word + 'ed')
#     else:
#         past_t.append(word+'d')
#     print(past_t)

# n=['Ivan','Pavel','Jordan']
# while True:
#     print('{}'.format(n[0::2]))

# n=['Ivan','Pavel','jordan']
# while True:
#     new=input('Кого добавим: ')
#     n.append(new)
#     print(n)


nomer=[]
name=[]
u=[]
w=1
while w==1:
    print('1-Добавить номер\n2-Добавть имя\n3-Добавить услугу')
    new=input('Выберите одно 1,2 или 3: ')
    if new=='1':
        new=input('Ведите номер:')
        nomer.append(new)
        print(nomer)
    elif new=='2':
         a=input('Ведите имя: ')
         name.append(new)
         print(name)
    elif new=='3':
        a=input('Какую услугу вы хотите добавит')
        u.append(new)
        print(u)

