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
    pass

ans = int(input("Enter 1 for Termux 2 for kali: "))

if ans == 1:
    termux()
else:
    print("soon")
    exit()
