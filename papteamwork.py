import time
import os

tomb = [0, 0, 0, 0, 0, 0, 0, 0, 0]

print("1) 3a feladat")
print("2) 3b feladat")
print("3) 3c feladat")
print("4) 3d feladat")
print("5) Kilépés")
menu = int(input())
os.system("clear")
if menu == 1:
    print("3a feladat")
    print("1) kód inditása")
    print("2) értékek modositás!")
    menu = int(input())
elif menu == 2:
    print("3b feladat")
    print("1) kód inditása")
    print("2) értékek modositás!")
    menu = int(input())
elif menu == 3:
    print("3c feladat")
    print("1) kód inditása")
    print("2) értékek modositás!")
    menu = int(input())
elif menu == 4:
    print("3d feladat")
    print("1) kód inditása")
    print("2) értékek modositás!")
    menu = int(input())
elif menu == 5:
    print("viszlát!")
    time.sleep(3)
    exit
else:
    print("Jó számot adj meg!")
    
if menu== 2:
    for i in range(len(tomb)):
        ujszam = input()
        tomb[i] = ujszam
        
    print(tomb)
#else:
   # itt fog futni a kód