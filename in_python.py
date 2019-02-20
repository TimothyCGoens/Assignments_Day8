file_object = open("learning_python.txt", "w")

with open("learning_python.txt", "w") as file_object:
    file_object.write("""In Python you can create dictionaries.
In Python you can loop.
In python you can create classes.
""")

with open("learning_python.txt") as file_object:
    contents = file_object.read()
    print(contents)
    print(contents)
    print(contents)

with open("learning_python.txt") as file_object:
    for line in file_object:
        print(line)

with open("learning_python.txt", "a") as file_object:
    file_object.write("In Python I can do anything! \n")
    file_object.write("In Python I am struggling! \n")
