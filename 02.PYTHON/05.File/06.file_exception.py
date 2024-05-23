try:
    with open("file.txt", "r") as file:
        contents = file.read()

    print(contents)
except FileNotFoundError:
    print("No File")
except PermissionError:
    print("No Permission")
