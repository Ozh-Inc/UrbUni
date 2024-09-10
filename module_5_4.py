class House:

    def __new__(cls, *args, **kwargs):
        if len(args) > 0:
            cls.houses_history.append(args[0])
        elif kwargs.get('name') is not None:
            cls.houses_history.append(kwargs['name'])
        else:
            print('Error')
        return object.__new__(cls)

    def __init__(self, name: str, floors: int):
        self.name = name
        self.number_of_floors = floors

    houses_history = []

    def go_to(self, target_floor: int, alt_method = False):
        if target_floor < 1 or target_floor > self.number_of_floors:
            print('Ну попробуй. Такого этажа не существует.')
            return
        if alt_method == False:
            print(list(range(1, target_floor + 1)))
        else:
            for i in range(1, target_floor + 1):
                print(i)

    def __del__(self):
        print(f'{self.name} - снесён, но он останется в истории.')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __add__(self, val):
        if isinstance(val, int):
            self.number_of_floors += val
            return self

    def __iadd__(self, val):
        if isinstance(val, int):
            self.number_of_floors += val
            return self

    def __radd__(self, val):
        if isinstance(val, int):
            self.number_of_floors += val
            return self

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return True

Z = House('Igor Olegovich', 1489)
V = House('Viktor ValerieVICH', 2)
Z.go_to(7, True)
Z.go_to(1487)
V.go_to(3)

#__str__
print(str(Z))
print(str(V))

#__len__
print(len(Z))
print(len(V))

print(Z)
print(V)

#__eq__
print(V == Z)

#__add__
V = V + 1487
print(V)
print(V == Z)

#__iadd__
V += 1487
print(V)

#__radd__
Z = 12 + Z
print(Z)

print(V > Z) # __gt__
print(Z >= V) # __ge__
print(V < Z) # __lt__
print(Z <= V) # __le__
print(V != Z) # __ne__

O = House(name='Georgiy Brusnikov', floors= 12)

print(House.houses_history)

del O

a = input(' ')
