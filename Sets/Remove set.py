# Remove items remove() / discard() method
fruits_set = {'apple','mango','bananas','cheery','coconut'}
print(fruits_set)
fruits_set.remove('mango')
print(fruits_set)
# Discard() method
fruits_set.discard("cheery")
print(fruits_set)
fruits_set.discard("cheery")
print(fruits_set)
fruits_list=['jackfruit','pineapple','orane']
fruits_set.update(fruits_list)
print(fruits_set)
# using pop() method this method remove random item
x = fruits_set.pop();
print(x)
print(fruits_set)

# clear method()
fruits_set.clear()
print(fruits_set)

# delete method()
print(fruits_set)
del fruits_set