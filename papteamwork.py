import time
import os
import random
menu = 0
tomb=[]
while menu!=5:


    if menu== 0:
        print("┬ ┬┌─┐┬  ┬  ┌─┐┬ ")                                                 
        print("├─┤├┤ │  │  │ ││ ")                                                   
        print("┴ ┴└─┘┴─┘┴─┘└─┘o ")                                                   
        print("┬  ┬┌─┐│┬  ┌─┐┌─┐┌─┐┌─┐  ┌─┐┌─┐┬  ┌─┐┌┬┐┌─┐┌┬┐┌─┐┌┬┐ o")                                                                                                                
        print("└┐┌┘├─┤ │  ├─┤└─┐└─┐┌─┘  ├┤ ├┤ │  ├─┤ ││├─┤ │ │ │ │ ") 
        print(" └┘ ┴ ┴ ┴─┘┴ ┴└─┘└─┘└─┘  └  └─┘┴─┘┴ ┴─┴┘┴ ┴ ┴ └─┘ ┴  o")
        print("______________________________________________________")                                                     
        print("1) 3a feladat")
        print("2) 3b feladat")
        print("3) 3c feladat")
        print("4) 3d feladat")
        print("5) Kilépés")
        menu = int(input())
    
    os.system("cls")

    if menu == 1:
        
        print("3a feladat")
        n=int(input("n:"))
        m=int(input("m:"))
        for i in range(n*m):
            # ujszam = input()
            ujszam = random.randint(1,10)
            tomb.append(ujszam)
        print(tomb)
        menu = 0
    elif menu == 2:
        print("3b feladat")
        n=int(input("n:"))
        m=int(input("m:"))
        for i in range(n*m):
            # ujszam = input()
            ujszam = random.randint(1,10)
            tomb.append(ujszam)
        print(tomb)
        menu = 0
    elif menu == 3:
        print("3c feladat")
        n=int(input("n:"))
        m=int(input("m:"))
        for i in range(n*m):
            # ujszam = input()
            ujszam = random.randint(1,10)
            tomb.append(ujszam)
        print(tomb)
        menu = 0
    elif menu == 4:
        print("3d feladat")
        n=int(input("n:"))
        m=int(input("m:"))
        for i in range(n*m):
            # ujszam = input()
            ujszam = random.randint(1,10)
            tomb.append(ujszam)
        print(tomb)
        menu = 0
    elif menu == 5:
        print('')
    else:
        print("Jó számot adj meg!")

os.system("cls")
print("viszlát!")   
exit
