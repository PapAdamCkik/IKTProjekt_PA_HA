import time
print("1) 3a feladat")
print("2) 3b feladat")
print("3) 3c feladat")
print("4) 3d feladat")
print("5) Kilépés")
menu = int(input())
if menu == 1:
    print("3a feladat")
elif menu == 2:
    print("3b feladat")
elif menu == 3:
    print("3c feladat")
elif menu == 4:
    print("3d feladat")
elif menu == 5:
    print("viszlát!")
    time.sleep(3)
    exit
else:
    print("Számot adj meg!")