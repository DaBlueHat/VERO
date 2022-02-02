import os

with open('VeroBoot\VeroBoot.VERO') as A:
    print("Loading VeroBoot")
    VeroBoot = A.read()

    if VeroBoot == "0":
        print("Loading VeroSetup")
        os.startfile('VEROSETUP.py')

    if VeroBoot == "1":
        print("Loading VeroLogin")
        os.startfile('VeroLogin.py')