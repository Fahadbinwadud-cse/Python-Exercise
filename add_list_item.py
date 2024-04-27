# append method
mylist = ['apple','mango','cherry','jamrul']
mylist.append('coconut')
print(mylist)
# insert item
mylist.insert(1,'orange')
print(mylist)
# extend list
new_list = ['banana','watermelon','pineapple']
mylist.extend(new_list)
print(mylist)
# add any iterable
thistuple = ('Jamun','papaya')
mylist.extend(thistuple)
print(mylist)