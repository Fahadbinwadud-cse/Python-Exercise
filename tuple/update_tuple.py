# change tuple value
mytuple = ("apple","bananas","jackfruit","cherry")
mylist = list(mytuple)
mylist.remove("jackfruit")
print(mylist)
mytuple = tuple(mylist)
print(mytuple)

# add items in tuple
mytuple = ("apple","bananas","jackfruit","cherry")
mylist = list(mytuple)
mylist.append("pineapple")
mytuple = tuple(mylist)
print(mytuple)

# add tuple to a tuple
thistuple = ("Ford","BMW","Lamborghini")
newtuple = ('Toyota','Volvo','Audi','Mercedes')
thistuple += newtuple
print(thistuple)

# remove item in tuple
mylist = list(thistuple)
mylist.pop(3)
print(mylist)
# Or you can delete tuple completely
print(mytuple)
del mytuple
