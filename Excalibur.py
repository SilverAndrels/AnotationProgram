from os import system as sy
while True:
    sy("clear")
    print("-" * 66)
    print("Program made for help with some anotations by WhoamiSilver v.0.0.2")
    print("-" * 66)
    anotations = input("Input your anotation: ")
    if anotations == "exit":
        sy("clear")
        break
    else:
        with open("ant.txt", "a") as file:
            file.write(anotations + "\n")
            sy("clear")