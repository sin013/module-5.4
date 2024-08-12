class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.floors = int(floors)

    def go_to(self, new_floor):
        int(new_floor)
        if new_floor > self.floors or new_floor < 1:
            print(f'В доме "{self.name}" этажа №{new_floor} не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.floors}')

    def __eq__(self, other):
        return self.floors == other.floors

    def __lt__(self, other):
        return self.floors < other.floors

    def __le__(self, other):
        return self.floors <= other.floors

    def __gt__(self, other):
        return self.floors > other.floors

    def __ge__(self, other):
        return self.floors >= other.floors

    def __ne__(self, other):
        return self.floors != other.floors and self.name != other.name

    def __add__(self, other):
        self.floors += other
        return self

    def __radd__(self, other):
        self.floors += other
        return self

    def __iadd__(self, other):
        self.floors += other
        return self

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
h4 = House('ЖК Чебуреки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
