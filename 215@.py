import re

text ="The ghost that says boo hanuts the loo"
m =re.findall(".oo",text,re.IGNORECASE)
print(m)
