import json

# some json
x = '{"name":"Mahmud","age":28,"city":"Dhaka"}'
y = json.loads(x)
print(y["name"])