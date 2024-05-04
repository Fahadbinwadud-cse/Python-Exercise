car = {
    "brand":"Ford",
    "model":"mustang",
    "year":1964
}
my_car = car.copy()
print(my_car)
# another way to copy building function
my_new_car = dict(my_car)
print(my_new_car)