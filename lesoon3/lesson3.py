class Human:
    def __init__(self, name): #constructor
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passengers_names(self):
        if self.passengers != []:
            print(f"\nNames of {self.brand} passengers.")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print("There are no passengers in " + self.brand)


murad = Human("Murad shalunishka teddy foxy")
guseyn = Human("Chat gptshnik aye qaqash")
elmir = Human("Xuliqan")
ulvi = Human("Yaxshi oqlan")
jamil = Human("Mandarinka")
mika = Human("genius millioner")
muradAliyev = Human("Aliyev aqilli adam")
jalal = Human("good player")
melek = Human("Strong woman")
sulik = Human("Suslik")

bmw = Auto("BMW M5")
byd = Auto("BYD")
jiguli = Auto("07")



bmw.add_passenger(murad, melek, mika, muradAliyev)
byd.add_passenger(jamil, jalal)
jiguli.add_passenger(guseyn, ulvi, elmir, sulik)

bmw.print_passengers_names()
byd.print_passengers_names()
jiguli.print_passengers_names()
