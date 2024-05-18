class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move..!!")
class Car(Vehicle):
    pass
class Boat(Vehicle):
    def move(self):
        print("Sail")
class Plane(Vehicle):
    def move(self):
        print("Fly..!!")
car_obj = Car("Ford","Mustang")
boat_obj = Boat("Ibiza","Touring 20")
plane_obj = Plane("Boeing","747")
for x in (car_obj,boat_obj,plane_obj):
    print(x.brand)
    print(x.model)
    x.move()