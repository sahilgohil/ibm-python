def write_to_file(str):
    with open("output.txt","w") as file:
        file.write(str)

def read_from_file():
    with open("output.txt","r") as file:
        print(file.read())

write_to_file("Hello, World!")
read_from_file()