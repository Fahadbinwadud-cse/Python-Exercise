# loop through access in the list
fruits_list = ["apple","banana","cheery","mango"]
for x in fruits_list:
    print(x)
# loop through a string
for x in "pineapple":
    print(x)
# break statement
print("continue break statement : ")
for x in fruits_list:
    if x == 'cheery':
        break
    print(x)
# Continue Statement
print("continue statement : ")
for x in fruits_list:
    if x == 'banana':
        continue
    print(x)
# range() function
print("Using range function : ")
for x in range(6):
    print(x)
# for range limit 2 to 6
print("Range 2 to 6")
for x in range(2,6):
    print(x)
# increment the sequence with 3
print("increment the sequence with 3")
for y in range(2,30,5):
    print(y)
# using else condition
for x in range(6):
    print(x)
else:
    print("finally finished...!!")
#  Using break statement
for x in range(5):
    if x==3:
        break
    print(x)
else:
    print("Finally finished...!!")
# Nested Loop
adj = ['red','tasty','big']
fruit_list = ['apple','watermelon','pineapple']
for x in adj:
    for y in fruit_list:
        print(x," : ",y)

# The pass statement
for x in range(8):
    pass
print("Finally Finished")