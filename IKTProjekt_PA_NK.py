import time  # Modul az idő kezelésére
import os  # Modul az operációs rendszer funkcióinak eléréséhez
import random  # Modul véletlenszám-generáláshoz

menu = 5  # Menü alapértelmezett értéke
menu2 = 0  # Almenü alapértelmezett értéke
tomb = []  # Üres lista, amelyet a program különböző feladatokhoz használ
times = 1  # Számláló, amely a menü előzményeit követi
sleep = int(3)  # Időkésleltetés másodpercekben

# A menü addig fut, amíg a felhasználó ki nem lép (menu == 6)
while menu != 6:

    # Menü inicializálása, ha a menu értéke 0
    if menu == 0:
        os.system("cls")  # A képernyő törlése (Windows rendszereken)
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
        menu = int(input())  # Felhasználói választás

    os.system("cls")  # A képernyő törlése

    # 3a feladat megvalósítása
    if menu == 1:
        print("3a feladat")
        print(tomb)
        f1tomb = []  # Átmeneti lista az eredményekhez
        f1m = -1
        kutya1 = 0
        lepes = 0
        i = 0

        # Az abszolút győztes kiszámítása
        for v in range(m):
            while lepes != n:
                kutya1 += tomb[i]
                i += 1
                lepes += 1
            f1tomb.append(kutya1)
            lepes = 0
            kutya1 = 0
        print(f1tomb)

        # Legnagyobb érték keresése
        maxi = 0
        for i in range(0, len(f1tomb), 1):
            if f1tomb[i] > f1tomb[maxi]:
                maxi = i
        abszgyku = maxi
        print(abszgyku + 1)

        # Újraszámítás a győzelem kategóriái alapján
        f1tomb.clear()
        futas = 0
        gyozelem = 0
        for l in range(n):
            f1tomb.clear()
            i = futas
            while i < len(tomb):
                f1tomb.append(tomb[i])
                i += n
            print(f1tomb)
            futas += 1

            # Győztes keresése
            maxi = 0
            for k in range(1, len(f1tomb), 1):
                if f1tomb[maxi] < f1tomb[k]:
                    maxi = k
            if f1tomb[abszgyku] == f1tomb[maxi]:
                gyozelem += 1
        print(f"Az abszolút győztes kutya {gyozelem} kategóriában nyert")
        menu = 0
        time.sleep(sleep)

    # 3b feladat megvalósítása
    elif menu == 2:
        print("3b feladat")
        print(tomb)
        f2tomb = []
        f2m = -1

        # Kategóriák átlagértékeinek kiszámítása
        for i in range(n):
            kutya1 = 0
            f2m += 1 
            for i in range(f2m, len(tomb), n):
                kutya1 += tomb[i]
            kutya1 = round(kutya1 / m, 2)
            f2tomb.append(kutya1)

        # Kategóriák kiírása
        sorszam = 0
        while sorszam != n:
            print(f"{sorszam+1}. kategória: {f2tomb[sorszam]}")
            sorszam += 1
        menu = 0
        time.sleep(sleep)

    # 3c feladat megvalósítása
    elif menu == 3:
        print("3c feladat")
        print(tomb)
        f3m = 0

        # Szebb kutyák számlálása
        for i in range(n):
            i += n
            if tomb[i] > tomb[i + 1]:
                f3m += 1
        print(f"{f3m} kutya volt inkább szebb, mint okos.")
        menu = 0
        time.sleep(sleep)

    # 3d feladat megvalósítása
    elif menu == 4:
        print("3d feladat")
        print(tomb)
        f4tomb = []
        f4m = 0

        # Eredmények kiszámítása
        for i in range(1,len(tomb),n):
            for s in range (n):
                f4m += tomb[s+i-1]
            f4tomb.append(f4m)
            f4m=0

        print(f4tomb)

        # Legnagyobb érték ellenőrzése
        maxi = 0
        for i in range(0, len(f4tomb), 1):
            if f4tomb[i] > f4tomb[maxi]:
                maxi = i

        db = 0
        for i in range(0, len(f4tomb), 1):
            if f4tomb[i] == f4tomb[maxi]:
                db += 1

        if db > 1:
            print('igen.')
        else:
            print('nem.')
        menu = 0
        time.sleep(sleep)

    # Beállítások menü
    elif menu == 5:
        if times == 1:
            print("┬ ┬┌─┐┬  ┬  ┌─┐┬ ")                                                 
            print("├─┤├┤ │  │  │ ││ ")            
            print("┴ ┴└─┘┴─┘┴─┘└─┘o ")
            print("Elösször töltsd fel a tömböt!")
        if times > 1:
            print("Tömb módosításai:")

        print("1) Feltöltés randommal")
        print("2) Feltöltés billentyűzetről")
        if times > 1:
            print("3) Tömb adott számának módosítása")
            print(f"4) Várakozási idő (Az várakozás ideje jelenleg: {sleep})")
            print("kilépés: A felsoroltakkon kívül bármelyik számmal ")
            print()
            print("Tömb tartalma:", tomb)
        
        menu2 = int(input())  # Felhasználó almenü választása
        # Ha az első használatkor érvénytelen a választás
        if times == 1 and (menu2 < 1 or menu2 > 2):
            if tomb == []:  # Ha a lista üres, újraindítja a menüt
                menu = 5
                times = 1

        # Ha érvénytelen a választás már módosított állapotban
        elif times == 2 and (menu2 < 1 or menu2 > 4):
            menu = 5
            times = 2

        else:
            # 1) Véletlenszerű számokkal tölti fel a tömböt
            if menu2 == 1:
                n = int(input("n:"))  # Kategóriák száma
                m = int(input("m:"))  # Kategóriánkénti számok száma
                tomb = []
                for i in range(n * m):  # Lista feltöltése véletlenszerű számokkal
                    ujszam = random.randint(1, 10)  # Szám 1 és 10 között
                    tomb.append(ujszam)

            # 2) Billentyűzetről történő feltöltés
            elif menu2 == 2:
                n = int(input("n:"))  # Kategóriák száma
                m = int(input("m:"))  # Kategóriánkénti számok száma
                print("10 és 1 között kell számot megadnod!")
                tomb = []
                for i in range(n * m):  # Felhasználói input alapján tölt fel
                    ujszam = int(input())
                    tomb.append(ujszam)

            # 3) Egy adott elem módosítása (csak ha korábban már van tömb)
            elif menu2 == 3 and times == 2:
                modositani = int(input("Módosítandó szám helye:"))
                számmodositás = int(input(f"A tömb {modositani}. elemének száma legyen:"))
                if 1 <= számmodositás <= 10:  # Ellenőrzi, hogy 1 és 10 között van-e az érték
                    tomb[modositani - 1] = számmodositás  # A megadott indexen módosítja az elemet
                else:
                    print('10 és 1 között kell számot megadnod!!')
                    time.sleep(sleep)

            # 4) Várakozási idő beállítása
            elif menu2 == 4:
                sleep = int(input("Várakozási idő:"))

            # Visszatér a főmenübe
            menu = 0
            times = 2

    # 6) Kilépés
    elif menu == 6:
        print('')

    # Érvénytelen választás esetén a menü visszaállítása
    else:
        menu = 0

# Kilépés előtti üzenet
os.system("cls")  # A képernyő törlése
print("Viszlát!")


print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%##@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%##**#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##****%@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%###******#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*******#@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%##*********@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#**********#@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##********++*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#************#@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#********+++*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%***++++++******#@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*******++++++#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#****++++++++++**%@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*******+++++++*@@@@@@@@@@@@@@@@@@@@@@@@@@#**+++++++++++++++*@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#******++++++++++%@@@@@@@@@@@@@@@@@@@@@@%**++++++++++++++++*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*******++++++++++*@@@@@@@@@@@@@@@@@@@@%****++++++=++++++++*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*******+++++++++*#@@@@@@@@@@@@@@@@@@@@%#**+++++===++++++*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#******#%%@@@@@@@@@@@@@@@@@@@@@%%%%%####****++++=+++=-=*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#***********+++++++++++++++++++++++++-:%@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*****+++++++++++++++++=====+=====++++++=....=@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#***+++++++++++==++=========================:.....+@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#***+++++++++================-------------===+++..=@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*+++++++++++=============--------::--::----=+++%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+++++++++++++======-------------:::::::::::-=++*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*+*#%%%#***++*++===-------===++++*==----::::-==+*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+#@@@@@@@@@@@@#**++==--:::-=+%@@@@@@@@#=-=-::--=+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@%:..=@@#++=-:::-=*@@@@@@@+...+%---.:-==*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=....*@@*==-:::-+@@@@@@@%.....@@---:-==+*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*-:.-@@*=--::..*@@@@@@@%*-...%@#.+==-=++++**#@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*+::#@%=--:...*@@@@@@@#*+=:-#@#.=+=-=====++++*%@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*++#@#+-::...=@@@@@@@%**+=*%@*.++=======+++++%@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##%%*==--::..-#@@@@@@@%###%#+.:----=====++*%@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#**+++*%@%*+===++++====-::=+++==::.........:--====+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**#@@@@@%+---:-=*+=--:..=+++-:............:--===#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@*+-:::.:=*+=--=++=-:.............:-===+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@%+=--::::-+===++=-::..==:......::----==+*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*+===--*%%#*+==-::-*+-::::::---=----==+++++*%@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%####%@@@@@@@@@@@@@@%*=-:::::---====----====++++*@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*++==--=+#@@@@@@%*+-:::::::::--===========++#%@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*+++====------=----::::::::::--=========+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**+++======-------:::::::::::::--====++#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**++========----:::::::::::::--====+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+++======--------:-----::::::-----=%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*+++======---------------:::::-----=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*++=======----------------------====#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%**++=========------------------====+=*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**+++++=========--------===========++++%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#**+++++==========================+++++**@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#**++++++++++================+++++++++***%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%***++++++++++++==========++++++++++++****#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*****++++++++++++++++++++++++++++********#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")