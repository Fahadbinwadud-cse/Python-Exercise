# Remove specified item
thislist = ['apple','grape','papaya','cherry','coconut','watermelon','jamrul','pineapple']
thislist.remove('papaya')
print(thislist)
# remove specified index
thislist.pop(1)
print(thislist)
# Remove last item
thislist.pop()
print(thislist)
# delete whole list
del thislist
thislist = ['apple','grape','papaya','cherry','coconut','watermelon','jamrul','pineapple']
print(thislist)
# Delete specified index
del thislist[0]
print(thislist)
# clear the list
thislist.clear()
print(thislist)