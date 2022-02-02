import os


with open(r'USER\username.VERO', 'r+') as A:
    print("Welcome to the vero setup")
    UserSet = input("Enter the username You want to use: ")
    A.write(UserSet)

with open(r'USER\password.VERO', 'r+') as B:
    PassSet =  input("Enter the password you want to use: ") 
    B.write(PassSet)

with open(r'VeroBoot\VeroBoot.VERO', 'r+') as C:
    print("Setup complete!")
    C.write('1')
    os.startfile('VERO.py')