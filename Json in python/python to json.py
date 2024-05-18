import json
my_dic = {
    "name":"Fahim",
    "age":28,
    "designation":"Engineer"
}
x = json.dumps(my_dic)
print(x)