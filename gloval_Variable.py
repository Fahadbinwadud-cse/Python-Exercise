x = 'awesome'


def myfunc():
    global x
    x = 'fantastic'
    print("python is " + x)


myfunc()
print("python is " + x)
