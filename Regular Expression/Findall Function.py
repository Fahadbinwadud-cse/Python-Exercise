import re

txt = "The rain in Bangladesh"
x = re.findall("Bangladesh",txt)
print(x)
# No match are found an empty list is return
