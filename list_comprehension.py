# list of comprehension
fruits_list = ['apple','banana','mango','coconut','pineapple']
new_list = []
for x in fruits_list:
    if 'a' in x:
        new_list.append(x)
print(new_list)
# you can do one line code
new_fruits =[x for x in fruits_list if 'a' in x]
print(new_fruits)
# condition
new_fruits_item = [x for x in fruits_list if x != 'apple']
print(new_fruits_item)
# without condition
new_fruits_items = [x for x in fruits_list]
print(new_fruits_items)
# iterable object using range()
new_items = [x for x in range(len(fruits_list))]
print(new_items)
# Expression
newlist = [x.upper() for x in fruits_list]
print(newlist)
# set new value in list
new_list_one = ['fahmida' for x in fruits_list]
print(new_list_one)
# 'apple' instead of 'banana'
new_list_two = [x.upper() if x!='apple' else 'Orange' for x in fruits_list]
print(new_list_two)