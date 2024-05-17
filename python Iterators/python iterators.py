# iterators method
my_tuple = ("apple","banana","Orange","cherry")
my_item = iter(my_tuple)
print(next(my_item))
print(next(my_item))
print(next(my_item))
# string are iterable object
my_string = "String"
my_str_item =iter(my_string)
print(next(my_str_item))
print(next(my_str_item))
print(next(my_str_item))
print(next(my_str_item))
print(next(my_str_item))
print(next(my_str_item))
# Looping through an iterator
for x in my_tuple:
    print(x)
for x in my_string:
    print(x)
# Create a iterator that returning numbers
class Mynumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
my_obj = Mynumber()
my_items = iter(my_obj)
print(next(my_items))
print(next(my_items))
print(next(my_items))
print(next(my_items))
print(next(my_items))

# Stop iteration
class Myclass:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <=20 :
            y = self.a
            self.a += 1
            return y
        else:
            raise StopIteration
my_num_obj = Myclass()
item_iter = iter(my_num_obj)
for x in item_iter:
    print(x)
