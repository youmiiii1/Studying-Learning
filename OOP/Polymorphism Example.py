class Vehicle:
    def __init__(self, color, price):
        self.speed = 0
        self.color = color
        self.price = price

class Motorbike(Vehicle):
    def __init__(self, color, price):
        super().__init__(color, price)
        self.speed = 120

    def drive_on(self):
        return f"{self.__class__.__name__} drive on {self.speed} KMh."

class Plane(Vehicle):
    def __init__(self, color, price):
        super().__init__(color, price)
        self.speed = 750

    def drive_on(self):
        return f"{self.__class__.__name__} fly on {self.speed} KMh."

temp = [
Motorbike("White", 300),
Plane("Black", 1000)
]

for vehicle in temp:
    print(vehicle.drive_on())
