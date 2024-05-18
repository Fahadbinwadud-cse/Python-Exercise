def myfunc():
    x = "January"
    def innerfunc():
        nonlocal x
        x ="I'm a nonlocal string"
    innerfunc()
    return x
print(myfunc())