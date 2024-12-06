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
        os.system("clear")                                       
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
    
    os.system("clear")

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
        abszgyku=maxi
        print(abszgyku+1)
        f1tomb.clear()
        f1m=n
        sorszam=0
        i=0
        nyert=0
        l=0
        for l in range (m):
            f1tomb.clear()
            while i!=f1m:
                f1tomb.append(tomb[i])
                i+=1
            f1m+=n
            maxi=0
            k=0
            for k in range(0,len(f1tomb),1):
                if f1tomb[k]>f1tomb[maxi]:
                    maxi=k
            db=0
            u=0
            if maxi==abszgyku:
                for u in range(0,len(f1tomb),1):
                    if f1tomb[u]==f1tomb[maxi]:
                        db+=1
                if db == 1:
                    print(f"{sorszam+1}. kategóriában: Nyert")
                    nyert+=1
                else:
                    print(f"{sorszam+1}. kategóriában: Döntetlen")
                
            else:
                for u in range(0,len(f1tomb),1):
                    if f1tomb[u]==f1tomb[maxi]:
                        db+=1
                if db == 1:
                    print(f"{sorszam+1}. kategóriában: nem nyert")
                else:
                    print(f"{sorszam+1}. kategóriában: Döntetlen")
            sorszam+=1
            
        print(f"Az abszolút győztes kutya {nyert} kategóriában nyert. ")
        menu = 0
        time.sleep(sleep)
    elif menu == 2:
        print("3b feladat")
        print(tomb)
        f2tomb=[]
        f2m=-1
        kutya1=0
        for i in range (n):
            kutya1=0
            f2m+=1
            for i in range(f2m, len(tomb), n):
                kutya1+=tomb[i]
            kutya1=round(kutya1/m, 2)
            f2tomb.append(kutya1)
        sorszam=0
        while sorszam!=n:
            print(f"{sorszam+1}. kategória: {f2tomb[sorszam]}")
            sorszam+=1
        menu = 0
        time.sleep(sleep)



    elif menu == 3:
        print("3c feladat")
        print(tomb)
        db=1
        f3m=-1
        f3tomb=[]
        for i in range (n):
            kutya1=0
            f3m+=1
            for i in range(f3m, len(tomb), n):
                f3tomb.append(tomb[i])
            if f3tomb[1]>f3tomb[2]:
                db+=1
            print(f3tomb)
            f3tomb.clear()
        print(f"{db} kutya volt inkább szebb, mint okos.")
        


        menu = 0
        time.sleep(sleep)
    elif menu == 4:
        print("3d feladat")
        print(tomb)
        f4tomb=[]
        f4m=0
        holtverseny=0
        for i in range(0,n,1):
            for i in range(f4m, len(tomb), n ):

                f4tomb.append(tomb[i])
                legnagyobb=f4tomb[0]

            for i in range(1,len(f4tomb),1):
                if legnagyobb<f4tomb[i]:
                    legnagyobb=f4tomb[i]

            if f4tomb.count(legnagyobb)>=2:
                holtverseny+=10
                    
            f4m+=1
            f4tomb.clear()        
        if holtverseny>1:
            print('igen.')
        else:
            print('nem.')
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
        if times==1 and menu2 < 1 or times==1 and menu2 > 2:
            if tomb==[]:
                menu = 5
                times = 1
        elif times==2 and menu2 < 1 or times==1 and menu2 > 4:
            menu=5
            times=2
        else:
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
        menu=0
    

os.system("clear")
print("viszlát!")