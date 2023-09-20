# a=lambda x: x**2
# print(a(10))
#
# b=lambda y,u:y+u
# print(b(2,3))

# a=lambda x:x*2
# print(a(5))

# def spam2(a,b,c=7):
#     print(a+b+c)
# spam2(3,5)

# def spam2(a,b):
#     print(a+b)
# spam2(2,3)

# all_p={'Склад':{'name':'хлеб',
#                 'arg':32}}
# def get_p(a):
#     print(all_p['Склад'][a])
# get_p('name')
#
# def get_p(a='name'):
#     print(all_p['Склад'][a])
# get_p()

# def spam1(*args):
#     return args
# print(spam1(1,2,3,4))
#
# def spam1(*args):
#     for i in args:
#         print(i)
# spam1(1,2,3,4,5,6)
# while True:
#     def nums():
#         i=int(input('Введите число которое хотите проверит: '))
#         if i%2==0:
#             print('ЧЕтное')
#         elif i%2!=0:
#             print('нечетное')
#     nums()
clients={}
open_room=[i for i in range(1,21)]
closed_room=[]




