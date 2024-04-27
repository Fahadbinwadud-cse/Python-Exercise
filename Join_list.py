# join two list
list_one = ['a','b','c']
list_two = [1,2,3]
list_three = list_one + list_two
print(list_three)

# Another way join two list
for x in list_two:
    list_one.append(x)
    print(list_one)

# using extend() method for joining two list
list_one.extend(list_three)
print(list_one)
x = list_one.count('a')
print(x)