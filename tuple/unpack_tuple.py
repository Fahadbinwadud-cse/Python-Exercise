# Packing a tuple
fruits = ("apple","plum","water apple")
print(fruits)

# unpacking a tuple
(green,red,white) = fruits
print(green,red,white)

# Using Asterisk* symbol
cars = ("Ford","BMW","Audi","Lamborghini","Mercedes")
(*black,blue,green) = cars
print(black)
print(blue)
print(green)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

