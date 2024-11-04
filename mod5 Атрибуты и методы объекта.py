class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('This floor does not exist')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'ЖК Акация 15: {self.name}, количество этажей: 15'
h1 = House('ЖК Эльбрус', 30)
h2 = House('ЖК Акация', 15)

print(str(h1))
print(str(h2))
print(len(h1))
print(len(h2))
