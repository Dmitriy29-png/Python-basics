
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

    def turn_direction(self):
        return f'{self.name} is turned right'

class TownCar(Car):

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')
        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'

class SportCar(Car):
            pass

class WorkCar(Car):
    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')
        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for work car'

class PoliceCar(Car):

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department of Orizona'
        else:
            return f'{self.name} is not from police department'

aston_martin = SportCar(180, 'silver', 'Aston Martin', False)
skoda = TownCar(70, 'white', 'Skoda Kodiaq', False)
kraz = WorkCar(50, 'orange', 'KrAz 260', False)
ford = PoliceCar(60, 'Blue', 'Ford', True)
print(skoda.turn_direction())
print(f'When {skoda.turn_direction()}, then {kraz.stop()}')
print(f'{skoda.go()} with speed exactly {skoda.show_speed()}')
print(f'{kraz.name} is {kraz.color}')
print(f'Is {aston_martin.name} a police car?: {aston_martin.is_police}')
print(f'Is {skoda.name}  a police car?: {skoda.is_police}')
print(aston_martin.go())
print(skoda.show_speed())
print(ford.police())
print(kraz.show_speed())
