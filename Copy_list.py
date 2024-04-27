# copy list using copy() method
thislist = ['apple','jackfruit','pineapple']
mylist = thislist.copy()
print(mylist)

# copy list another way using list() method
thislist.append('cherry')
new_list = list(thislist)
print(new_list)
