#Author : Vishvesh Mehd
from playsound import playsound
import random
from colorama import Faore, Back, Style, init
init(autoreset=True)
li = []
for i in range(1, 91):
    li.append(i)
li1 = []
li1 = random.sample(li, 90)
x = '''[ 1  2  3  4  5  6  7  8  9  10 ]\n[ 11 12 13 14 15 16 17 18 19 20 ]\n[ 21 22 23 24 25 26 27 28 29 30 ]\n[ 31 32 33 34 35 36 37 38 39 40 ]\n[ 41 42 43 44 45 46 47 48 49 50 ]\n[ 51 52 53 54 55 56 57 58 59 60 ]\n[ 61 62 63 64 65 66 67 68 69 70 ]\n[ 71 72 73 74 75 76 77 78 79 80 ]\n[ 81 82 83 84 85 86 87 88 89 90 ]\n'''
newx = Fore.RED + x
print(newx)
for i in range(0, 90):
    print("Current Number Is :", Fore.CYAN +
          str(li1[i]) + Style.RESET_ALL, "Press Enter and Wait While Music Is Playing...")
    y = str(li1[i])
    y = y+' '
    newy = Fore.GREEN + y + Fore.RED
    newx = newx.replace(y, newy, 1)
    wait = input("Press Enter to continue.")
    q = 22
    q = str(q)
    p = 'C:/Users/admin/Desktop/music/'
    p = p+q
    p = p+'.mp3'
    playsound(p)
    print(newx)
