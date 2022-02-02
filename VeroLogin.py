import os

with open(r'USER\password.VERO') as A:
    password = A.read()
    Unlock = input('Enter your password: ')

    if Unlock == password:
        print("unlocked")
        os.startfile('VeroAI.py')

    if Unlock != password:
        print("Invalid password")
        os.startfile('VeroLogin.py')