import json

filename = "names.json"

# user_name = input("What is your name? ")
#
# with open(filename, "w") as file_object:
#     json.dump(user_name, file_object)
#
# with open(filename) as file_object:
#     name = json.load(file_object)
#     print(name)


first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
dictionary = {"First Name": first_name, "Last Name": last_name}

with open(filename, "w") as file_object:
    json.dump(dictionary, file_object)

with open(filename) as file_object:
    names = json.load(file_object)
    print(names)
