#List Comprehension

# name='PAsha'
# n=[x for x in name]
# print(n)

# nums=[i for i in range(100)]
# print(nums)


# nums=[i for i in range(1,11)]
# chotnie=[num for num in nums if num %2 ==0]
# nechotnie=[num for num in nums if num %2 !=0]
# print(chotnie,nechotnie)

# n=['Pavel','Sasha','Jordan','PAsha']
# a=[i[0] for i in n]
# print(a)

# nums=[i for i in range(1,21)]
# chotnie=[num for num in nums if num %2 ==0]
# print(chotnie)

usernames=[]

u=input('Что вы хотите сделать посмотреть список 1 записать свой username 2: ').lower()

while True:
    if u=='1':
        print(usernames)
    elif u=='2':
        n1=input('Введите усер найм')
        if n1 in usernames:
            print('Такой имя уже есть')
        else:
            usernames.append(n1)


