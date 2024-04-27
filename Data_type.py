# if you want to the data type is set when you assign a value to a variable
x = "Hello Python"
x = 20
x = 7.07
x = 1j
x = ['apple', 'banana', 'orange']
x = ('cherry','pineapple','watermelon')
x = range(7)
x = {"name":"Fahad", "age": 30}
x = {'apple', 'cherry', 'orange'}
x = frozenset({'Hamid', 'Robin', 'Kibriya'})
x = True
x = b"Hello"
x = bytearray(7)
x = memoryview (bytes(5))
x = None
# print(type(x))
# if you want to specify the data type :
y = str("Hello Python")
y = int(20)
y = float(7.07)
y = complex(10j)
y = range(10)
y = dict(name="Fahad", age=20)
y = set(("fahad", 22 , 'Seventy'))
y = frozenset(("apple", "orange", "Mango"))
y = bool(11)
y = bytes(5)
y = bytearray(5)
y = memoryview(bytes(5))
print(y)

# int
x = 2
y = 230924802480284
z = -28087295734957934579
print(type(x))
print(type(y))
print(type(z))
# float
a = 7.0
b = 77.340384034803
c = -7.07
print(type(a))
print(type(b))
print(type(c))

# e and E to indicate the power of 10
a = 2e3
b = 3E4
c = 7.32e3
print(type(a))
print(type(b))
print(type(c))

# Complex
x = 3+2j
y = 5j
z = -2-3j
print(type(x))
print(type(y))
print(type(z))
# Type Conversion, Conver from one type to another:
x = 2
y = 3.33
z = -7j
a = float(x)
b = int(y)
c = complex(x)
print(a, b, c)
import random
print(random.randrange(1,10))



