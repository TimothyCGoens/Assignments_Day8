file_object = open("like_programming.txt", "w")
filename = "like_programming.txt"

user_input = ("Why do you like to program? ")

while user_input != "":
    with open("like_programming.txt", "a") as file_object:
        file_object.write(user_input)
    break
