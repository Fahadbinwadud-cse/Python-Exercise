# call __init__() function
class Persion:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Persion("Hamid",29)
print("He/She name & age are : ",p1.name,p1.age)
# __str__()
class Persion_details:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age
    def __str__(self):
        return f"{self.fname}{self.lname}({self.age})"
my_obj_one = Persion_details("Sipon ","Ahmed",28)
print(my_obj_one)
# Object methods
class PersionTwo:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def my_function(self):
        print("This man name & age are ",self.name,self.age)
obj_one = PersionTwo("Ayman",7)
obj_one.my_function()
# The self Parameter
class Myclass:
    def __init__(mysillyobject,fullname,num_age):
        mysillyobject.fullname = fullname
        mysillyobject.num_age = num_age
    def myfunc(a):
        print("this persion name is : ",a.fullname,a.num_age)
myObj = Myclass("Foysal Hossain",34)
print(myObj.fullname,myObj.num_age)
myObj.myfunc()
myObj.num_age=10
print(myObj.num_age)
del myObj.num_age
del myObj
# The pass Statement
class Lastclass:
    pass