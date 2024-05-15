# create a parent class
class Persion:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print("This is : ",self.fname,self.lname)
my_obj = Persion("Sujon","Hossain")
my_obj.printname()
# Create a child class
class Student(Persion):
    # pass
# call super function
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        # add properties
        self.graduationyear = year
#   Add method
    def my_method(self):
        print("Welcome",self.fname,self.lname,"to the class of ",self.graduationyear)

student_obj = Student("Ridoy","Khan",2019)
student_obj.printname()
print(student_obj.graduationyear)
student_obj.my_method()

