def myfunc():
    global x
    x = 96
    print("inside function x value is ",x)
myfunc()
print("Outside of the function x value is : ", x)
# x value is change when declare global inside the function
y = 100
def myfunc():
    global y
    y = 96
    print("inside declare global y value is ",y)
print("Before function call in x value is : ",y)
myfunc()
print("after function call in x value is : ",y)
