class Vehicle:
    __C0l0R_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self, model):
        return f'Модель: {self.__model}'

    def get_horse_power(self, engin_power):
        return f'Мощность двигателя:{self.__engine_power}'

    def get_color(self, color):
        return f'Цвет:{self.__color}'

    def print_info(self):
        print(self.get_model(''))
        print(self.get_horse_power(int()))
        print(self.get_color(''))
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in [color.lower() for color in self.__C0l0R_VARIANTS]:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


Vehicle1 = Sedan('Fedos', 'Toyota Mark II ', 500, 'blue')
Vehicle1.print_info()

Vehicle1.set_color('Pink')
Vehicle1.set_color('BLACK')
Vehicle1.owner = 'Vasyok'

Vehicle1.print_info()
