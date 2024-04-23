class TransportVehicle:
    def __init__(self, speed):
        self.speed = speed

    def movement(self):
        print("The vehicle is moving at a speed of", self.speed, "km/h")


class Car(TransportVehicle):
    def __init__(self, speed):
        super().__init__(speed)


class Bicycle(TransportVehicle):
    def __init__(self, speed):
        super().__init__(speed)


class Airplane(TransportVehicle):
    def __init__(self, speed):
        super().__init__(speed)



car = Car(100)
car.movement()

bicycle = Bicycle(20)
bicycle.movement()

airplane = Airplane(900)
airplane.movement()