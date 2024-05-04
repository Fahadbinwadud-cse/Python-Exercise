# Create a dictionary
this_dict = {
    'brand': 'Ford',
    'model':'mustang',
    'year': 1964
}
print(this_dict)
# Dictionary items
print(this_dict['model'])
# duplicates not allowed
this_dict = {
    'brand': 'Ford',
    'model':'mustang',
    'year': 1964,
    'year':2020
}
print(this_dict)

# dictionary length
dic_length = len(this_dict)
print(dic_length)
# The values in dictionary items can be any data type
this_dict_one={
    "brand":"Ford",
    "model":"mustang",
    "year":1964,
    "color":['red','green','black']
}
print(this_dict_one)
# Dictionary data type
print(type(this_dict_one))
# Dictionary constructor dict()
my_dict = dict(name='fahad',age=28,gender='Male')
print(my_dict)


