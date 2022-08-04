from os import system as sy
import pyautogui as py
while True:
    sy("cls")
    print("-" * 67)
    print("Program made for help with some anotations by SilverAndrels v.0.0.3")
    print("-" * 67)
    anotations = input("Input your anotation: ").lower()
    if anotations == "exit":
        sy("cls")
        break
    if anotations == "read":
        py.hotkey('win', 'r')
        py.write('C:/ProgramData/dist/ant.txt')
        py.press('enter')
    else:
        with open("C:/ProgramData/dist/ant.txt", "a") as file:
            file.write(anotations + "\n")
        sy("cls")
