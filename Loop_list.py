# Loop through in a list
thislist = ['mango','banana','grape','papaya']
for x in thislist :
    print(x)
# loop through the index number
for x in range(len(thislist)):
    print(thislist[x])
# Using a while loop
thislist = ['watermelon','mango','banana','grape','papaya']
i = 0
while i < len(thislist) :
    print(thislist[i])
    i += 1
# looping using list comprehension
[print(x) for x in thislist]
