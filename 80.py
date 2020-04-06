my_dict=dict()
my_dict2={}

f_color={"Banana":"yellow","Apple":"red"}
print(f_color)

f_color["Mikan"]="orange"
print(f_color)
print(f_color["Mikan"])

print("Banana" in f_color)
print("yellow" in f_color)

del f_color["Apple"]
print(f_color)
