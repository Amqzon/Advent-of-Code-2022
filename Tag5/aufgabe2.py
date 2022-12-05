with open("Tag5/ship.txt","r") as cargo_bay:
    # anfang vom daten parsen
    bay1 = {}
    bay2 = {}
    anzahl_zeile = []
    zahler = 1
    for zeile in cargo_bay:
        try:
            zahl = int(zeile[1])
            if type(zahl) == int:
                for nummer in zeile:
                    if nummer == " ":
                        pass
                    else:
                        anzahl_zeile.append(int(nummer))
                    for i in anzahl_zeile:
                        if i >=9:
                            anzahl_zeile.pop(-1)
                        else:
                            bay1["zeile" + str(i)] = []
        except:
            pass

    # den datei "zurückspulen" und bei zeile 0 wieder anfangen
    
    cargo_bay.seek(0)
    lerzeichen_zahler = 0
    for zeile in cargo_bay:
        for s in zeile:
            if zahler == anzahl_zeile[-1]+1:
                break
            if s == "\n":
                #neue zeile
                zahler += 1
            else:
                if (s == "[") or (s == "]"):
                    continue
                elif s == " ":
                    lerzeichen_zahler += 1
                    if lerzeichen_zahler == 4:
                        # alle nicht belegten auf frei setzen
                        bay1["zeile" + str(zahler)].append("FREI")
                        print(bay1["zeile" + str(zahler)])
                        lerzeichen_zahler = 0
                        
                        continue
                else:
                    bay1["zeile" + str(zahler)].append(s)
                    bay2["bay"+ str(zahler)] = []
                    lerzeichen_zahler = 0
                    continue

    #for zeile in bay1:
    #    print(bay1[zeile])
    
    bay_zahler = 1
    zum_hinzufuegen =[]
    ende = False
    while ende == False:
        try:
            if len(list(bay1)[-1]) == 0:
                ende = True
            for bay in bay1:
                zum_hinzufuegen.append(bay1[bay][0])
                bay1[bay].pop(0)


            # add reversed list to bay2
            k = []
            for i in zum_hinzufuegen:
                if i == "FREI":
                    pass
                else:
                    k.append(i)
                zum_hinzufuegen = k
            bay2["bay"+ str(bay_zahler)] = zum_hinzufuegen[::-1]
            zum_hinzufuegen = []
            bay_zahler += 1
            
        except IndexError:
            ende = True
    # ende vom daten parsen :/
    print(bay2)

with open("Tag5/ladeverlauf.txt", "r") as verlauf:
    for zeile in verlauf:
        aufgeteilt = zeile.split(" ")
        menge = int(aufgeteilt[1])
        start = int(aufgeteilt[3])
        ziel = int(aufgeteilt[5])
        kran_arm = []

        for container in range(menge):
            
            kran_arm.append(bay2["bay"+str(start)][-1])
            bay2["bay"+str(start)].pop(-1)
            
        kran_arm = kran_arm[::-1]
        for container in kran_arm:
            bay2["bay"+str(ziel)].append(container)
        
    print(bay2)
    solution = ""
    for zeile in bay2:
        
        solution = solution + bay2[zeile][-1]
            
print(f"Das ergebnis ist = {solution}")