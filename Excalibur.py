from os import system as sy
while True:
    sy("cls")
    print("-" * 66)
    print("Program made for help with some anotations by SilverAndrels v.0.0.2")
    print("-" * 66)
    anotations = input("Input your anotation: ")
    if anotations == "exit":
        sy("cls")
        break
    with open("ant.txt", "a") as file:
        file.write(anotations + "\n")
    sy("cls")
