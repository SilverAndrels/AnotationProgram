from os import system as st
st("clear")
print("-" * 67)
print("Program made for help with some anotations by SilverAndrels v.0.0.3")
print("-" * 67)
anotations = input("Input your anotation: ").lower()
with open("/home/whoamisilver/bin/ant.txt", "a") as file:
    file.write(anotations + "\n")
st("clear")
