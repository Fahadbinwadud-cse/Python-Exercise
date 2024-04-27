# Sort list alphanumerically
fruits = ['orange','apple','pineapple','jackfruit','mango','banana']
fruits.sort()
print(fruits)

# sort list numerically
numlist = [1,4,2,6,35,32,6,7,9]
numlist.sort()
print(numlist)

# sort descending order
fruits.sort(reverse=True)
numlist.sort(reverse=True)
print(fruits)
print(numlist)

# customize sort function
def myfunc(n):
    return abs(n - 50)
number_list = [100,50,65,82,23,99,6]
number_list.sort(key=myfunc)
print(number_list)

# case sensitive sort
fruits_list = ['jackfruit','mango','apple','Orange','Lemon','Pineapple']
fruits_list.sort(key = str.lower)
print(fruits_list)

# Reverse order
fruit_list = ['apple','pineapple','mango','lemon']
fruit_list.reverse()
print(fruit_list)
