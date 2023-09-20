# class Animal:
#     def __init__(self,cow,cat,dog):
#         self.cow=cow
#         self.cat=cat
#         self.dog=dog
# class Cow(Animal):
#     def __init__(self,cow,dog,cat):
#         super().__init__(cow,dog,cat)
#     def make_sound(self):
#         print('Muuuu')
# class Cat(Animal):
#     def __init__(self,cow,dog,cat):
#         super().__init__(cow,dog,cat)
#     def make_sound(self):
#         print('Miau')
# class Dog(Animal):
#     def __init__(self,cow,dog,cat):
#         super().__init__(cow,dog,cat)
#     def make_sound(self):
#         print('Gaf,Gaf')
#
# cows=Cow('cow','cat','dog')
# cows.make_sound()
#
# cows=Cat('cow','cat','dog')
# cows.make_sound()
#
# cows=Dog('cow','cat','dog')
# cows.make_sound()


# class Vehicle:
#     def __init__(self,brand,year):
#         self.brand=brand
#         self.year=year
# class Car(Vehicle):
#     def __init__(self,brand,year):
#         super().__init__(brand,year)
#     def display_info(self,brand,year):
#         print(brand,year)
# class Motorcycle(Vehicle):
#     def __init__(self,brand,year):
#         super().__init__(brand,year)
#     def display_info(self,brand,year):
#         print(brand,year)
# car1=Car('ravon','2021')
# print(car1.brand,car1.year)
#
# car1=Motorcycle('ducati','2023')
# print(car1.brand,car1.year)


