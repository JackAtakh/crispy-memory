n=[]
new=input('Напишите слова палиндром: ')
p= new.casefold()
r = reversed(p)
if list(p) == list(r):
    print('палиндор')
else:
    print('Не палиндор')


