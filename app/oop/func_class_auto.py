class Driver:
    full_name = None
    driving_experience = None

    def __init__(self, full_name: str, driving_experience: int):
        self.full_name = full_name
        self.driving_experience = driving_experience


class Engine:
    power = None
    manufacturer = None

    def __init__(self, power: str, manufacturer: str):
        self.power = power
        self.manufacturer = manufacturer


class Car(Driver, Engine):
    brand = None
    class_auto = None
    weight = None

    def __init__(self, full_name: str, driving_experience: int, power: str, manufacturer: str, brand: str, class_auto: str, weight: str):
        Driver.__init__(self, full_name, driving_experience)
        Engine.__init__(self, power, manufacturer)
        self.brand = brand
        self.class_auto = class_auto
        self.weight = weight

    def start(self):
        return "Поїхали"

    def stop(self):
        return "Зупиняємось"

    def turn_right(self):
        return "Поворот праворуч"

    def turn_left(self):
        return "Поворот ліворуч"

    def __str__(self):
        return f'Інфо: {self.full_name}, {self.driving_experience}, {self.power}, {self.manufacturer}, {self.brand}, {self.class_auto}, {self.weight}'


class Lorry(Car):
    carrying_capacity = None

    def __init__(self, full_name: str, driving_experience: int, power: str, manufacturer: str, brand: str, class_auto: str, weight: str, carrying_capacity: str):
        Car.__init__(self, full_name, driving_experience, power, manufacturer, brand, class_auto, weight)
        self.carrying_capacity = carrying_capacity

    def __str__(self):
        return f'Вантажопідйомність {self.carrying_capacity}'


class SportCar(Car):
    max_speed = None

    def __init__(self, full_name: str, driving_experience: int, power: str, manufacturer: str, brand: str, class_auto: str, weight: str, max_speed: str):
        Car.__init__(self, full_name, driving_experience, power, manufacturer, brand, class_auto, weight)
        self.max_speed = max_speed

    def __str__(self):
        Car.__str__(self)
        return f'Максимальна швидкість {self.max_speed}'


if __name__ == '__main__':
    car1 = Car('Harry Potter', 20, '400 horse power', 'MAN', 'MAN 24', 'Lorry', '20 ton')
    print(car1)
    car1 = Lorry('Harry Potter', 20, '400 horse power', 'MAN', 'MAN 24', 'Lorry', '20 ton', '10 ton')
    print(car1)
    print(car1.turn_left())
    car2 = Car('Oliver Harris', 10, '800 horse power', 'FORD', 'Ford Mustang', 'Sport Car', '5 ton')
    print(car2)
    car2 = SportCar('Oliver Harris', 10, '800 horse power', 'FORD', 'Ford Mustang', 'Sport Car', '5 ton', '336 miles')
    print(car2)
    print(car2.turn_left())
