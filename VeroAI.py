import os
import datetime
import platform
import time
import webbrowser

def VERO():
    AI = input("Please enter a command: ")

    match AI:
        case "Calculate my grades":
            Grade = input("Please enter your grade: ")
            match Grade:
                case "A":
                    print("You did Great")
                case "B":
                    print("You did Okay")
                case "C":
                    print("You did Bad")
                case "D":
                    print("You did terrible")
                case "E":
                    print("You did Very Very Bad")
                case "F":
                    print("You did super bad")
            VERO()
        case "What time is it":
            now = datetime.datetime.now()
            print("The time is")
            print(now.strftime("%Y-%m-%d and " + "%H:%M:%S"))
            VERO()
        case "neofetch":
            print("System specs")
            print(f"Computer network name: {platform.node()}")
            print(f"Machine type: {platform.machine()}")
            print(f"Processor type {platform.processor()}")
            VERO()
        case "web":
            print("Web Browser")
            print("-------------------------Web Browser--------------------------")
            print("##############################################################")
            print("##############################################################")
            print("##############################################################")
            print("##############################################################")
            print("##############################################################")
            print("--------------------------------------------------------------")
            web = input("Web URL: ")
            time.sleep(0.5)
            os.system('cls')
            print("-------------------------Web Browser--------------------------")
            print("##############################################################")
            print("##############################################################")
            print("##############################################################")
            print("##############################################################")
            print("##############################################################")
            print("----------------------WEB URL = " + web + "----------------------")
            webbrowser.open(web)

with open(r'VeroBoot\VeroBoot.VERO') as A:
    
    if A != "0":
        print("Verifed")
        VERO()
    
    if A == "0":
        print("Error")
        os.startfile('VeroAI.py')
