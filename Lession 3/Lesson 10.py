# class Animal:
#     def make_sound(self,s):
#         print(s)
#
#
# class Horse(Animal):
#     pass
#
#
# pony=Horse()
# pony.make_sound('Igogogo')
#
#
# class Parent:
#     def do(self):
#         pass
# class Rebenok(Parent):
#     pass
#
#
# class Car:
#     def __init__(self,model,color,year):
#         self.model=model
#         self.color=color
#         self.year=year
#
# class SuperCar(Car):
#     def __init__(self,model,color,year,sponsor):
#         super().__init__(model,color,year)
#         self.sponsor=sponsor
#
#
# class MyClass:
#     @classmethod
#     def say_hello(cls):
#         print('Hello, World!')
# MyClass.say_hello()


# class Recten:
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     @property
#     def area(self):
#         return self.width*self.height
# recteng=Recten(4,5)
# print(recteng.area)
#
# recteng.width=6
# print(recteng.area)


# class Worker:
#     def __init__(self,name,job):
#         self.name=name
#         self.job=job
# class Moder(Worker):
#     def __init__(self,name,job):
#         super().__init__(name,job)
#     def Show_Worker(self,name):
#         return name.job
# work_show=Worker('john','Directer')
# pavel=Moder('PAvel','Moder')
# print(pavel.job(john))


class Player:
    def __init__(self,stamina,power,accuracy,speed):
        self.stamina=stamina
        self.power=power
        self.accuracy=accuracy
        self.speed=speed
class Attacker(Player):
    def __init__(self,stamina,power,accuracy,speed):
        super().__init__(stamina,power,accuracy,speed)
    def goal(self,):
        print('Забил гол')
class Def(Player):
    def __init__(self,stamina,power,accuracy,speed):
        super().__init__(stamina,power,accuracy,speed)
    def defind(self):
        print('Отобрал мяч')
class PoluDef(Player):
    def __init__(self,stamina,power,accuracy,speed):
        super().__init__(stamina,power,accuracy,speed)
    def Polu(self):
        print('Попытался забрать мяч')
class Varat(Player):
    def __init__(self,stamina,power,accuracy,speed):
        super().__init__(stamina,power,accuracy,speed)
    def Vara(self):
        print('Словил мяч')
        






