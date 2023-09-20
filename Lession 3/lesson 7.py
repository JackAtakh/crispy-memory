# def calc() :
#     # print(3+5)
#     pass
# calc()
import requests
link='https://browser-info.ru/'
data={'comments':'Blabla',
      'custname':'Jack',
      'custemail':'elon@gmail.com',
      'custtel':'998907654321',
      'delivery':'21:00',
      'size':'large',
      'topping':'cheese'}
response=requests.post(link,data=data)
print(response.status_code)

