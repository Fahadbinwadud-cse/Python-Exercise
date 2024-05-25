import  re
txt = "I'm a python programmer"
x = re.sub('\s',"07",txt)
# Replace all white-space with digital character
print(x)
# Replace the first two occurrences
x = re.sub('\s',"  ",txt,2)
print(x)