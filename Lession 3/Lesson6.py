# x={'name':'Pasha',
#    'job':'TGbot'}
# print(x['name'])

# d={'name':['Jordan','Pavel'],
#    'age':(12,21),
#    'job':'programmers'}
# print(d['name'][0],d['job'][-1])

# i={'name':'Jordan',
#    'age':21,
#    'job':'prog'}
# print(i.items())

# i={'name':'Jordan',
#     'age':21,
#     'job':'prog'}
# if 'name' in i:
#     print('Да')
# else:
#     print('Не пон')

# user={}
# user['name']='Jordan'
#
# print(user)
# print(user['name'])

# my_dict={'name':'Jordan'}
# my_dict['name']='Pasha'
#
# print(my_dict)

# my_dict={'song':'Godzilla','singer':'Eminem'}
# my_dict.clear()
# print(my_dict)
#
# my_dict={'song':'Godzilla','singer':'Eminem'}
# my_dict.pop('song') #по ключу
# print(my_dict)

# my_dict={'song':'Godzilla','singer':'Eminem'}
# my_dict.popitem()#ключ и значения последние
# print(my_dict)

# name={'names',1,2,3,4,5}
# print(name)

# my=['2','33','33',2,'TGbot']
# my2=set(my)
# print(my2)

# instructer=dict(name='jordan',age=32,job='python prog',)
# for k in instructer.keys():
#     print(k)#'name'
              #'age'
              #'job'
# for k in instructer.values():
#     print(k)#'jordan'
              #'32'
              #'python prog'
# for k,v in instructer.items():
#     print(k,v)#'name' 'jordan'
            #age       '32'
            #job        'python prog'

# day=input('Введите праздник: ')
# praxdnik=dict(Навруз='21 march',
#               Newyear='1 december',)
# print(praxdnik.get(day))

all_p={'Весь склад':{}}
while True:
    ad=input('Что вы хотите сделать если вы хотите добавить что то в склад пишите д или хотите посмотреть скалд напиши с : ').lower()
    if ad=='д':
        a=input('Введите название продукта: ')
        b=input('Введите количесто продукта: ')
        all_p['Весь склад'][a]=b
        print(all_p)
    elif ad=='с':
        print(all_p)




