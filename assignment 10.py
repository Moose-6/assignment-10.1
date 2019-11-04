import os


directory =input("Hello, which directory would you like to access?")

if directory in dir(os):
    file = input("What file would you like to use?")

else:
    print("That file does not exist")


Name_user =input("Give us your name:")
Num_user =input("your number:")
Addr_user =input("and address:")

with open(file,'w') as file_object:
    file_object.write(f"{Name_user}")
    file_object.write(f"{Num_user}")
    file_object.write(f"{Addr_user}")


import json

file_input = [Name_user.title(), Num_user, Addr_user]

filename = 'file.json'
with open(filename, 'w') as f:
    json.dump(file_input, f)


with open(filename,) as f:
    file_input = json.load(f)


print(file_input)
    
