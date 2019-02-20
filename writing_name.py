file_object = open("guest.txt", "w")

user_name = input("Please enter your name: ")

with open("guest.txt", "w") as file_object:
    file_object.write(user_name)

    
