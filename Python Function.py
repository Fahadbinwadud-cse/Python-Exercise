def my_function():
    print("Hello from a function")
my_function()
# Arguments
def first_name(fname):
    print(fname + " Hossain")
first_name("Amir")
first_name("Shipon")
first_name("Ripon")
# Two numbers base on function
def full_name(f_name,l_name):
    print(f_name,l_name)
full_name("Fahad ","Bin Wadud")
full_name("Foysal","Bin Wadud")
# Arbitrary Arguments *arg
def arbitary_func(*name):
    print("Younger man name is : "+name[1])
arbitary_func("Mamun","Masum","Aman")
# Key word base argument
def key_argu_func(child1,child2,child3):
    print("First child name is : "+child1)
key_argu_func(child1="Rashed",child2="Foysal",child3="Alamin")
# Arbitrary key word argument **kwards
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
def my_function_one(**name):
    print("His first name is "+ name["fname"])
my_function_one(fname="Fahad",lname="Bin Wadud")
# Default parameter value
def country_func(country="Bangladesh"):
    print("This country name is "+country)
country_func()
country_func("india")
country_func("Pakistan")
country_func("Botan")
# Passing a list as an Argument
def my_list_pass_func(fruit):
    for x in fruit:
        print(x)
frutis = ["apple","pineapple","Guava","jackfruit"]
my_list_pass_func(frutis)
# Return keyword use in function
def my_mul_func(value_one,value_two):
    return value_one * value_two
print("The multiply value is : ", my_mul_func(2,3))
print("The multiply value is : ", my_mul_func(3,5))
# Pass empty function
def empty_func():
    pass
# Positional only argument
def positional_func(x,/):
    print(x)
positional_func(5)

def positional_func_one(x):
    print("The value is :", x)
positional_func_one(x=4)
# keyword only argument
def keyword_func(*,x):
    print(x)
keyword_func(x=77)
# combine positional only and keyword
def combine_positional_func(a,b,/,*,c,d):
    print("The sum of value is ", a+b+c+d)
combine_positional_func(2,3,c=4,d=9)

# Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
