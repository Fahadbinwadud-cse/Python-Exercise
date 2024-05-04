# nested dictionary
family = {
    "child_one" : {
    'name':"Abdur Rahman",
    'age' : 29
},
    "child_two" :{
        'name':"Ridika",
        'age':20
    },
    "child_three":{
        "name":"Ruble Hossain",
        "age":30
    }

}
print(family)
# another way nested dictionary
child_1 = {
    'name':'ayat',
    'age':6
}
child_2 ={
    'name':'aman',
    'age' : 4
}
my_family ={
    "child1":child_1,
    "child2":child_2
}
print(my_family)
# Access item dictionary
print(my_family["child1"]['name'])
print("new code execution : ")
# Loop through a nested dictionary
for x,obj in my_family.items():
    print(x)
    for y in obj:
        print(y)