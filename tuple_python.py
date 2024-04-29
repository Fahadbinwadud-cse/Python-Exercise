# create a tuple
this_tuple = ('Ford','BMW','Audi','Lamborghini','Fiat')
print(this_tuple)

# allow duplicates
this_tuple = ('Ford','BMW','Audi','Lamborghini','Audi')
print(this_tuple)

# tuple length
print("This tuple length is : ", len(this_tuple))

# create tuple with one item
my_tuple = ("Audi",)
print(type(my_tuple))
not_tuple = ("Lamborghini")
print(type(not_tuple))

# tuple data type
string_tuple = ("BMW","Ford","Lamborghini","Audi")
number_tuple = (2,4,6,712,46,77)
boolean_tuple = (True,False,True)

print(string_tuple,number_tuple,boolean_tuple)

# a tuple contain different data type
diff_tuple = ('BMW',23,True)
print(diff_tuple)

# type of tuple
print(type(diff_tuple))
print(type(boolean_tuple))

# The tuple() constructor
this_is_tuple = tuple(("apple","banana",23,35,True,False))
print(this_is_tuple)