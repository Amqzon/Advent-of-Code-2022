with open("Tag4/overlap.txt","r") as datei:
    zahler = 0
    for i in datei:
        # create two lists that contain range of numbers described
        healfte = i.split(",")
        aufgabe1 = healfte[0].split("-")
        aufgabe2 = healfte[1].split("-")

        umfang1 = []
        umfang2 = []
        
        for zahl in range(int(aufgabe1[0]),int(aufgabe1[1])+1):
            umfang1.append(zahl)
        for zahl in range(int(aufgabe2[0]),int(aufgabe2[1])+1):
            umfang2.append(zahl)
        
        
        
        vergleich = []
        vergleich2 = []
        for i in umfang1:
            if i in umfang2:
                vergleich.append(i)
            else:
                break
        
        for i in umfang2:
            if i in umfang1:
                vergleich2.append(i)
            else:
                break
        
        print(f"umfang1 {umfang1}")
        print(f"umfang2 {umfang2}")
        print(f"--------")
        print(f"vergleich {vergleich}")
        print(f"vergleich2 {vergleich2}\n")
        print("###########")


        if ((len(vergleich) > 0) or (len(vergleich2) > 0)):
            print("gefunden")

            print(umfang1)
            print(umfang2)
            print("----------")
            zahler += 1
    print(zahler)

