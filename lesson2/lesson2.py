class Student:
    def __init__(self, name, age,IQ):
        self.name = name # атрибут
        self.age = age
        self.IQ = IQ
        self.hp = 100

# Метод __init__ вызывается при создании объекта (экземпляра) класса.
# Он инициализирует (задает начальные значения) атрибуты объекта.

    def printer(self):
        print("name: " + self.name)
        print("age: " + str(self.age))
        print("IQ: " + str(self.IQ))
        print("hp: " + str(self.hp))

    def to_study(self):
        print("Time to study")
        self.hp -= 10
        self.IQ += 10

    def to_sleep(self):
        print("Zzzzzz....")
        self.hp +=5

    def to_chill(self):
        print("Chilling!!!")
        self.hp += 2

# Создаем трех студентов с разными параметрами.

first_student = Student(name = "Sosiska", age = 777, IQ= 5)
second_student = Student(name = "Murad", age = 14, IQ = 1)
third_student = Student(name = "Jamil",age = 2, IQ = 2 )


second_student.printer()

second_student.to_sleep()

second_student.printer()

second_student.to_study()

second_student.printer()


