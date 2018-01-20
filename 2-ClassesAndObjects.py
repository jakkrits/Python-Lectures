'''
Classes and Objects
'''

class Vehicle:
    def __init__(self, model, max_speed): # class constructor - should be no return statement
        self.model = model
        self.max_speed = max_speed
        self.speed = 0

    def turn_left(self):
        pass # pass = do nothing
    
    def turn_right(self):
        pass

    def accelerate(self, speed_difference):
        self.speed += abs(speed_difference)
        self.speed = min(self.speed, self.max_speed)

    def slow_down(self, speed_difference):
        self.speed -= abs(speed_difference)
        self.speed = max(self.speed, 0.01)

    def open_a_window(self):
        pass

class Car(Vehicle):
    pass

bmw_x6 = Car("BMW X6", 190)
bmw_x6.accelerate(5)
print(bmw_x6.speed)
bmw_x6.accelerate(17)
print(bmw_x6.speed)
bmw_x6.slow_down(100)
print(bmw_x6.speed)

class Bus(Vehicle):
    def slow_down(self, speed_difference):
        super().slow_down(speed_difference)
        self.speed = max(self.speed, 0)
        print(self.speed)

bus_a = Bus("Bus ขสมก", 80)
print(str(bus_a.speed) + " km/h " + bus_a.model)
bus_a.speed = 129
bus_a.slow_down(17)
print(bus_a.speed)

# bike is a subclass of vehicle, with max speed of 30
class Bike(Vehicle):
    def __init__(self, model, max_speed):
        self.max_speed = min(max_speed, 30)
        print(self.max_speed)
        super().__init__(model, max_speed)
    
    def show_status(self):
        print('This is {0} with {1} km/h'.format(self.model, str(self.max_speed)))

small_bike = Bike("ping ping's bike", 90)
print(small_bike.model, small_bike.max_speed)
small_bike.show_status()