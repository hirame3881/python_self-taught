import re

string ="Two too."
m =re.findall("t[wo]o",string,re.IGNORECASE)
print(m)



line ="123 hi 34 hello"
m =re.findall("\d",line,re.IGNORECASE)
print(m)



t ="__three__ __two__ __one__"
found =re.findall("__.*?__",t)
print(found)

u ="__three__two__one__"
found =re.findall("__.*?__",u)
print(found)
