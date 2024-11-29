import time
import os
import random
menu = 5  
menu2 = 0
tomb=[]
times=1
sleep=int(3)
while menu!=6:

    if menu== 0:
        os.system("cls")                                       
        print("┬  ┬┌─┐│┬  ┌─┐┌─┐┌─┐┌─┐  ┌─┐┌─┐┬  ┌─┐┌┬┐┌─┐┌┬┐┌─┐┌┬┐ o")                                                                                                                
        print("└┐┌┘├─┤ │  ├─┤└─┐└─┐┌─┘  ├┤ ├┤ │  ├─┤ ││├─┤ │ │ │ │ ") 
        print(" └┘ ┴ ┴ ┴─┘┴ ┴└─┘└─┘└─┘  └  └─┘┴─┘┴ ┴─┴┘┴ ┴ ┴ └─┘ ┴  o")
        print("______________________________________________________")                                                     
        print("1) 3a feladat")
        print("2) 3b feladat")
        print("3) 3c feladat")
        print("4) 3d feladat")
        print(f"5) Beállítások: {tomb}")
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
        time.sleep(sleep)
    elif menu == 2:
        print("3b feladat")
        print(tomb)
        f1tomb=[]
        f1m=-1
        kutya1=0
        for i in range (n):
            kutya1=0
            f1m+=1
            for i in range(f1m, len(tomb), n):
                kutya1+=tomb[i]
            kutya1=round(kutya1/m, 2)
            f1tomb.append(kutya1)
        sorszam=0
        while sorszam!=n:
            print(f"{sorszam+1}. kategória: {f1tomb[sorszam]}")
            sorszam+=1
        menu = 0
        time.sleep(sleep)
    elif menu == 3:
        print("3c feladat")
        print(tomb)
        menu = 0
        time.sleep(sleep)
    elif menu == 4:
        print("3d feladat")
        print(tomb)
        menu = 0
        time.sleep(sleep)
    elif menu == 5:
        if times==1:
            print("┬ ┬┌─┐┬  ┬  ┌─┐┬ ")                                                 
            print("├─┤├┤ │  │  │ ││ ")                                                   
            print("┴ ┴└─┘┴─┘┴─┘└─┘o ")
            print("Elösször töltsd fel a tömböt!")
        if times>1:
            print("tömb modositásai:")
        print("1) feltöltés randommal")
        print("2) feltöltés billentyüzetröl")
        if times>1:
            print("3) tomb adot számának modositása")
            print("beálitások:")
            print(f"4) Várakozási idő (Az várakozás ideje jeleneg: {sleep})")
            print( )
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
            print("10 és 1 között kell számot megadnod!")
            tomb = []
            for i in range(n*m):
                ujszam = int(input())
                tomb.append(ujszam)
        elif menu2==3 and times==2:
            modositani=int(input("Modositando szám helye:"))
            számmodositás=int(input(f"A tomb {modositani}. elemének száma legyen:"))
            if számmodositás<=10 and számmodositás>=1:
                tomb[modositani-1]=számmodositás
            else:
                print('10 és 1 között kell számot megadnod!!')
                time.sleep(sleep)
        elif menu2==4:
            sleep=int(input("Várakozási idő:"))
        menu=0
        times=2
    elif menu == 6:
        print('')
    else:
        print("Jó számot adj meg!")
    

os.system("cls")
print("viszlát!")