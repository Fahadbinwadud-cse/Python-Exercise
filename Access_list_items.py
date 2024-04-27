# indexing
thislist = ['apple','nut','orange','cherry','mango','lichu','watermelon']
print(thislist[0])
# Negative index
print((thislist[-1]))
# range of indexes & 3 index is not included
print(thislist[1:3])
# first 4 items
print(thislist[:4])
# 3 to end of items
print(thislist[3:])
# negative range
print(thislist[-4:-1])
# check exist item
if 'cherry' in thislist:
    print("Yes,cherry is in the exist fruits list")
else:
    print("Not,cherry is not in exist fruits list")
