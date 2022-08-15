import getpass
import sys
import pyAesCrypt
from os import stat, remove
from os import system as st
from time import sleep as slp
import pyautogui as py

def escrever():
    st("cls")
    while True:
        print("-" * 67)
        print("Program made for help with some anotations by SilverAndrels v.0.0.3")
        print("-" * 67)
        anotations = input("Input your anotation: ").lower()
        if anotations == "exit":
            st("cls")
            crypt()
        if anotations == 'ex':
            break
        if anotations == "read":
            py.hotkey('win', 'r')
            slp(0.5)
            py.write('notepad path')
            py.press('enter')
        else:
            with open("ant.rar", "a") as file:
                file.write("\n" + anotations)
        st("cls")

def crypt():
    bufferSize = 256 * 1024
    escolha = input('digite: \n1- Encript \n2- Decript\nR: ')
    if escolha == '3':
        escrever()
    else:
        password = getpass.getpass('\nDigite a Senha:')

    if escolha == '1':
        # encrypt
        with open("ant.rar", "rb") as fIn:
            with open("ant.rar.aes", "wb") as fOut:
                pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
        x = input('do you want to delete the txt file? y ')

        if x != 'y':
            print('\nok')
            slp(1)
            sys.exit()

        remove("ant.rar")
        print('Arquivo removido')
        slp(2)
        sys.exit()

    if escolha == '2':
        # get encrypted file size
        encFileSize = stat("ant.rar.aes").st_size

        # decrypt
        with open("ant.rar.aes", "rb") as fIn:
            try:
                with open("ant.rar", "wb") as fOut:
                    # decrypt file stream
                    pyAesCrypt.decryptStream(
                        fIn, fOut, password, bufferSize, encFileSize)
            except ValueError:
                print('senha incorreta')
                # remove output file on error
                remove("ant.rar")

        slp(3)
        remove('ant.rar.aes')
        sys.exit()
    
password = 'a1'
while True:
    choose = input('Escolha oque quer:')
    if choose == 'a1':
        choose = input('Escolha oque quer:')
        if (choose == '1'):
            escrever()
        elif (choose == '2'):
            crypt()
    else:
        break
