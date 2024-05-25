import  re
txt = "The rain in bangladesh"
x = re.search("\s",txt)
print("The first white-space character is location in position: ",x.start())