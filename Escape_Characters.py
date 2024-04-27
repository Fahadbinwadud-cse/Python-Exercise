# Single Quote
txt = "It\'s alright"
print(txt)
txt = "We are the so called\"Vikings\" from the north."
# Backslash
txt ="This will insert one \\ (blackslash)"
print(txt)
# new line
txt = "Hello\nworld"
print(txt)
#Carriage Return
tx = "I write\rsomethings"
print(tx)
# This example erases one character (backspace)
txt = "Hello \bpython"
print(txt)
# Using placehold
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
class myclass() :
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

# Function can return boolean values
def myFunction() :
    return False
if myFunction():
    print("Yes.!")
else:
    print("No")
x=300
print(isinstance(x,int))
