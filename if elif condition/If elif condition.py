x = 101
y = 100
if x > y:
    print(x, " is greater than ", y)
elif x == y:
    print(x, " is equal to ", y)
else:
    print(x, "is less than ", y)
# short hand if
if x == y: print(x, 'is equal to ', y)
print(x) if x > y else print(y)

# Three condition in one line
x = 15
y = 11
print(x) if x > y else print(x, " is equal to ", y) if x == y else print(y)

# using or , and operator
a = 5
b = 6
c = 10
if a > b and a > c:
    print(a, " is greater than ", b, " and ", c)
elif a < b and b > c:
    print(b, " is greater than ", a, " and ", c)
else:
    print(c, "is greater than ", a, " & ", b)
if a > b or a < c:
    print(a, " is less than ", b, " & ", c)
if not a > b:
    print("a is not greater than b")
# Nested if
if a < b:
    if a < c:
        print(c, " is greater than ", a, " & ", b)
    elif b > c:
        print(b, " is greater than ", a, " & ", c)
    else:
        print(a, " is greater than ", b, " & ", c)

if a < c:
    pass
