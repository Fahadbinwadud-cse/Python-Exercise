# reomve item
cars = {
    "Brand":"Ford",
    "Model":"Mustang",
    "year":1964,
    "color":"Yellow"
}
print(cars)
print(cars.pop("Model"))
print(cars)
# remove last item using popitems()
print(cars.popitem())
print(cars)
# using delete del keyword
del cars["year"]
print(cars)
# using clear method
cars.clear()
print(cars)
# delete whole dictionary
del cars
