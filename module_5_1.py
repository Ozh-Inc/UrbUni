class House:
    def __init__(self, name: str, floors: int):
        self.name = name
        self.number_of_floors = floors
    def go_to(self, target_floor: int, alt_method = False):
        if target_floor < 1 or target_floor > self.number_of_floors:
            print('Ну попробуй.')
            return
        if alt_method == False:
            print(list(range(1, target_floor + 1)))
        else:
            for i in range(1, target_floor + 1):
                print(i)

Z = House('Igor Olegovich', 1489)
V = House('Viktor ValerieVICH', 2)
Z.go_to(7, True)
Z.go_to(1487)
V.go_to(3)