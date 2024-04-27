# bitwise & (AND)
x = 2
y = 3
"""
x = 00000010
y = 00000011
"""
print(x & y)
# bitwise | (OR)
print(x | y)
# bitwise ^ (XOR)
print(x & y)
# bitwise ~ (NOT) inverts all bits
print(~3)
"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""
# left shift
x = 2
print(x << 2)
# right shift
x = 10
print(x >> 2)
