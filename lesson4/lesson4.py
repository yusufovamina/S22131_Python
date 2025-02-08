'''

class Human:
    height = 170

class Student(Human):
    height = 150

class Worker(Human):
    pass

murad = Student()
guseyn = Worker()

print(murad.height)
print(guseyn.height)

'''


'''

class GrandParent:
    height = 180
    age = 75
    eyecolor = "blue"
    haircolor = "blond"

class Parent(GrandParent):
    height = 190
    age = 40
    haircolor = "light brown"

class Child( Parent):
    height = 175
    age =20

elmir = Child()
print(elmir.height,elmir.eyecolor, elmir.haircolor, elmir.age)

'''
'''

class Animal:
    def about(self):
        print("I'm animal")

class Mammal(Animal):
    def about(self):
        print("I'm mammal")

class Dolphin(Mammal):
    def about(self):
        super().about()
        print("I'm dolphin")


dolphin = Dolphin()
dolphin.about()
'''


class Father:
    def __init__(self):
        super().__init__()
        self.iq = 130

class Mother:
    def __init__(self):
        super().__init__()
        self.iq = 140

class Child( Father,Mother):
    def print_info(self):
        print(self.iq)

child = Child()
child.print_info()