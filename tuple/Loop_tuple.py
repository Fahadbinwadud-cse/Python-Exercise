# loop through in a tuple
fruits_tuple = ('Apple','Bananas','Orange','Jackfruit')
for x in fruits_tuple:
    print(x)
# using range and len method
for i in range(len(fruits_tuple)):
    print(fruits_tuple[i])

# Using while loop for tuple
print("Using while in a tuple ")
k = 0
while k < len(fruits_tuple):
    print(fruits_tuple[k])
    k += 1
