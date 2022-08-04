from os import system as st
import pyautogui as pg
while True:
    st("cls")
    print("-" * 67)
    print("Program made for help with some anotations by SilverAndrels v.0.0.3")
    print("-" * 67)
    anotations = input("Input your anotation: ").lower()
    if anotations == "exit":
        st("cls")
        break
    if anotations == "read":
        pg.hotkey('win', 'r')
        pg.write('C:/ProgramData/dist/ant.txt')
        pg.press('enter')
    else:
        with open("C:/ProgramData/dist/ant.txt", "a") as file:
            file.write(anotations + "\n")
        st("cls")
