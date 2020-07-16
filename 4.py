class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


bmw = SportCar(100, 'White', 'BMW', False)
kia = TownCar(30, 'Red', 'Kia', False)
vw = WorkCar(70, 'Blue', 'VW', True)
chevy = PoliceCar(110, 'Black',  'Chevy', True)
print(vw.turn_left())
print(f'When {kia.turn_right()}, then {bmw.stop()}')
print(f'{vw.go()} with speed exactly {vw.show_speed()}')
print(f'{vw.name} is {vw.color}')
print(f'Is {bmw.name} a police car? {bmw.is_police}')
print(f'Is {vw.name}  a work car? {vw.is_police}')
print(bmw.show_speed())
print(kia.show_speed())
print(chevy.police())
print(chevy.show_speed())