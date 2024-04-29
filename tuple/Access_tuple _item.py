# access tuple item
my_tuple = ("apple","orange","mango","banana","jackfruit","blackberry","coconut")
print(my_tuple[0])

# Negative indexing
print(my_tuple[-1])

# Range of indexes
print(my_tuple[2:6])
print(my_tuple[:4])
print(my_tuple[2:])

# Negative range of indexes
print(my_tuple[-4:-1])
print(my_tuple[-6:])
# check if item exists
if "mango" in my_tuple :
  print("Yes, 'mango' is in the fruits tuple")
else:
    print("No,this item isn't exist int the item")