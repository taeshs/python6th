
class Car:
    wheels = 4

    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    #method
    def drive(self):
        return "The car is moving!"

    def stop(self):
        return "The car is stopped."


my_car = Car("Kia", "Morning", "blue")

print(my_car.make)

print(my_car.drive())
print(my_car.stop())