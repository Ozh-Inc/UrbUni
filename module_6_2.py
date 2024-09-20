class Vehicle:
    __COLOUR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner: str, model: str, engine_power: int, colour: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__colour = colour
    def get_model(self):
        return f'Model: {self.__model}'
    def get_horsepower(self):
        return f'Engine power: {self.__engine_power}'
    def get_colour(self):
        return f'Colour: {self.__colour}'
    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_colour(), f'Owner: {self.owner}', sep= '\n')
    def set_colour(self, new_colour: str):
        if new_colour.lower() in self.__COLOUR_VARIANTS:
            self.__colour = new_colour
            return
        print(f'Нельзя сменить цвет на {new_colour}')
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

vehicle1.print_info()

vehicle1.set_colour('Pink')
vehicle1.set_colour('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()