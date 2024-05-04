this_dic = {
    "brand":"Ford",
    "model":"mustang",
    "year":1964
}
print(this_dic["year"])
# get() another method
x = this_dic.get("model")
print(x)
# key() method
y = this_dic.keys()
print(y)

# add a new item in dictionary
cars = {
    "brand":"Ford",
    "model":"mustang",
    "year":1964
}
cars_keys = cars.keys()
print(cars_keys)
cars['color']='Black'
print(cars.keys())
# Get values
car_values = cars.values()
print(car_values)
# update value
# before
print(car_values)
# after
cars["year"] = 1900
print(cars)
cars['Fuel type'] = 'Petrol'
print(cars)
# items() method
# before
x = cars.items()
print("Before add key,value : ", x)
cars["Engine Displacement"]='4999 cc'
# after
print("After : ",   x)

# check key exist
if "model" in cars:
    print("Yes, model key is exist in the card dictionary")
else:
    print("No, model key doesn't exist in the card dictionary")