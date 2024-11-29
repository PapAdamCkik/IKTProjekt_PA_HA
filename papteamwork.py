import time
import os
import random
menu = 5
menu2 = 0
tomb=[]
while menu!=6:


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
        print(f"5) tömb modositása: {tomb}")
        print("6) Kilépés")
        menu = int(input())
    
    os.system("cls")

    if menu == 1:
        print("3a feladat")
        print(tomb)
        f1tomb=[]
        f1m=-1
        kutya1=0
        for i in range (n):
            kutya1=0
            f1m+=1
            for i in range(f1m, len(tomb), n):
                kutya1+=tomb[i]
            f1tomb.append(kutya1)
        print(f1tomb)
        maxi=0
        i=0
        for i in range(0,len(f1tomb),1):
            if f1tomb[i]>f1tomb[maxi]:
                maxi=i
        abszgyku=maxi+1
        print(abszgyku)
        kat=0
        katcheck=[]
        for i in range(tomb):
            katcheck.append(tomb(i))
            if i//n == i/n:
                print("todo remove this")
        menu = 0
    elif menu == 2:
        print("3b feladat")
        print(tomb)
        menu = 0
    elif menu == 3:
        print("3c feladat")
        print(tomb)
        menu = 0
    elif menu == 4:
        print("3d feladat")
        print(tomb)
        menu = 0
    elif menu == 5:
        print("tömb modositása")
        print("1) feltöltés randommal")
        print("2) feltöltés billentyüzetröl")
        print("tömb tartalma", tomb)
        menu2 = int(input())
        if menu2==1 :
            n=int(input("n:"))
            m=int(input("m:"))
            tomb = []
            for i in range(n*m):
                ujszam = random.randint(1,10)
                tomb.append(ujszam)
        elif menu2==2 :
            n=int(input("n:"))
            m=int(input("m:"))
            tomb = []
            for i in range(n*m):
                ujszam = int(input())
                tomb.append(ujszam)
        menu=0
    elif menu == 6:
        print('')
    else:
        print("Jó számot adj meg!")
    

os.system("cls")
print("viszlát!")