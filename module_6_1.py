class Animal:
    Alive = True
    Fed = False
    def __init__(self, name: str):
        self.name = name


class Plant:
    Edible = False
    def __init__(self, name: str):
        self.name = name

class Flower(Plant):
    Inedible = True
class Fruit(Plant):
    Edible = True

class Herbivore(Animal):
    def eat(self, food: Plant):
        if food.Edible is True:
            print(f'{self.name} съел {food.name}')
            self.Fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.Alive = False

class Omnivore(Animal):
    def eat(self, food: Plant):
        if food.Edible is True:
            print(f'{self.name} съел {food.name}')
            self.Fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.Alive = False


a1 = Omnivore('Omni')
a2 = Herbivore('Herbi')
p1 = Flower('Peppermint')
p2 = Fruit('Pepper')

print(a1.name)
print(p1.name)

print(a1.Alive)
print(a2.Fed)
a1.eat(p1)
a2.eat(p2)
print(a1.Alive)
print(a2.Fed)
