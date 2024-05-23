# open 파일 입출력을 할때

# with open("example.txt", "a") as file:
#     file.write("Hello, world \n")


# with open("example.txt", "r") as file:
#     r_text = file.read()
#     print(r_text)


with open("example.txt", "r") as file:
    for line in file:
        print(line, end="")
