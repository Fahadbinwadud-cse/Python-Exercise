cars = {
    "brand":"Ford",
    "model":"mustang",
    "year":1964,
    "color":"black"
}
# print all keys one by one
for x in cars:
    print(x)
# print all values one by one
for x in cars:
    print(cars[x])
print(cars.keys())
print(cars.values())
print(cars.items())
print("Cars keys are : ")
for car_key in cars.keys():
    print(car_key)
print("Cars values are : ")
for car_value in cars.values():
    print(car_value)
print("Cars items are : ")
for car_item in cars.items():
    print(car_item)