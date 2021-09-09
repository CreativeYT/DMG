import os
import time
def termux():
    os.system("pkg update")
    os.system("pkg upgrade")
    os.system("pkg install python")
    os.system("pkg install python2")
    os.system("pkg install python3")
    os.system("pkg install ruby")
    os.system("pkg install git")
    os.system("pkg install php")
    os.system("pkg install java")
    os.system("pkg install google")
    os.system("pkg install bash")
    os.system("pkg install perl")
    os.system("pkg install nmap")
    os.system("pkg install clang")
    os.system("pkg install macchanger")
    os.system("pkg install nano")
    os.system("pkg install figlet")
    os.system("pkg install cowsay")
    os.system("pkg install curl")
    os.system("pkg install tar")
    os.system("pkg install zip")
    os.system("pkg install unzip")
    os.system("pkg install tor")
    os.system("pkg install sudo")
    os.system("pkg install wget")
    os.system("pkg install wcalc")
    os.system("pkg install openssl")
    os.system("pkg install bmon")

def kali():
    os.system("sudo apt update")
    os.system("sudo apt upgrade")
    os.system("sudo apt install python")
    os.system("sudo apt install python2")
    os.system("sudo apt install python3")
    os.system("sudo apt install ruby")
    os.system("sudo apt install git")
    os.system("sudo apt install php")
    os.system("sudo apt install java")
    os.system("sudo apt install google")
    os.system("sudo apt install bash")
    os.system("sudo apt install perl")
    os.system("sudo apt install nmap")
    os.system("sudo apt install clang")
    os.system("sudo apt install macchanger")
    os.system("sudo apt install nano")
    os.system("sudo apt install figlet")
    os.system("sudo apt install cowsay")
    os.system("sudo apt install curl")
    os.system("sudo apt install tar")
    os.system("sudo apt install zip")
    os.system("sudo apt install unzip")
    os.system("sudo apt install tor")
    os.system("sudo apt install sudo")
    os.system("sudo apt install wget")
    os.system("sudo apt install wcalc")
    os.system("sudo apt install openssl")
    os.system("sudo apt install bmon")


os.system("clear")
print("**********************************************")
print("*  * * *         **    **         *****      *")
print("*  *    *        * *  * *        *           *")
print("*  *     *       *  **  *       *            *")
print("*  *     *       *      *       *   ****     *")
print("*  *    *        *      *        *    *      *")
print("*  * * *         *      *         ****       *")
print("**********************************************")
print("               Yossef W. Eldeeb               ")

print("\nUse to install all the important tools for termux or linux\n")

maxsum = 2

for i in range(maxsum):
    print("\n \nChoose the Operating System:- \n")
    print("1) Termux")
    print("2) Linux")
    print("3) Exit")

    user = int(input("\n: "))
 
    if user == 1:
        termux()
    elif user == 2:
        kali()
    elif user == 3:
        os.system("clear")
        break
    else:
        print("The Number isn't in the choose!")
