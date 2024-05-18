class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive.!!")
class Boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Sail..!!")
class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Fly..!!")
car_obj = Car("Ford","Mustang")
boat_obj = Boat("Ibiza","Touring 20")
plane_obj = Plane("Boeing","747")
for x in (car_obj,boat_obj,plane_obj):
    x.move()