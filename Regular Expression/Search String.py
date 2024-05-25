import  re
text = "The rain in bangladesh"
x = re.search("^The.*bangladesh$",text)
if x:
    print("Yes!!,We have a match")
else:
    print("No match")