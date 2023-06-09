
# class Car:
#
#
#     def start(self):
#         print("starting the car")
#
# car1 = Car() # car1 is a object of class car
# car2 = Car() # once the class created we can create multiple objects(indefinite)
#
# car1.start() # calling the one method available in class car

# constructor will identify the object

class Car:

    def __init__(self, make, model, year): # constructor with different attributes
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, increment):
        self.speed = self.speed + increment

    def stop(self):
        self.speed = 0
        print("Car is stopped")


car1 = Car("Mahindra", "xuv300", 2020)
car2 = Car("Maruti", "swift", 2021)

car1.accelerate(10)
car1.speed
car1.stop()

