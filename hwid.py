import ctypes
import string
import os
import time
import sys, time
from os import system, name

LICNECE = """
Registration System by ZXCGOD#3778
"""

ctypes.windll.kernel32.SetConsoleTitleA(b"SnikSlots - Registration")

print(LICNECE)
time.sleep(3)
def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)
sprint('[Server] Connecting to database. . .')
time.sleep(2)
sprint('[Server] Cheking db connection. . .')
time.sleep(2)
sprint('[Server] Launching. . .')
clear = lambda: os.system('cls')
clear()
time.sleep(3)
login = input("Введите логин: ")
password = input("Введите пароль: ")
passwordrepeat = input("Повторите пароль: ")
time.sleep(3)
print("Welcome " + str(login) + " good luck!")
input()