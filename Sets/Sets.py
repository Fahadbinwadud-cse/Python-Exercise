# Create a set
this_set = {'apple','mango','bananas'}
print(type(this_set))
print(this_set)
# Duplicates not allowed
my_set = {'apple','mango','bananas','apple'}
print(my_set) # not print duplicate value
# True and 1 is considered the same value
my_set={'apple','mango','bananas',True,1,2}
print(my_set)
my_set={'apple','mango','bananas',True,False,1,2,3}
print(my_set)
# Get the length of the set
print(len(my_set))
# set items - Data type
set_string = {'apple','mango','orange'}
set_number = {1,2,3,5}
set_bool = {False,True,False}
set_different = {True,'apple','mango',1,2,3,True}
print(set_string,set_number,set_bool,set_different)
# using type () method
print(type(set_different))
# The set constructor
my_set = set(('apple',False,27))
print(my_set)
