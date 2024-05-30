import re

my_string="start middle end"
pattern1=re.compile("^start")
pattern2=re.compile(" end")

print(pattern1.match(my_string))
print(pattern2.match(my_string))
