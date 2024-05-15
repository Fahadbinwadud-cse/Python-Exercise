# create a lambda function
add = lambda a : a + 10
print(add(5))
subtract = lambda a,b : a - b
print("The subtraction value is : ",subtract(6,2))
# summarize argument in lambda function
summarize = lambda a,b,c : a+b+c
print("The summarize values is : ",summarize(2,3,4))
# Function inside the lambda function
def my_func(n):
    return lambda num : num * n
double = my_func(6)
print(double(5))
# my Triple function
def my_triple_func(n):
    return lambda num1 : num1 * n
triple = my_triple_func(3)
print(triple(3))
#multiple using function
print(triple(5))