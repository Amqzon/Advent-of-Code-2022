import numpy as np
with open("Tag8/aufgabe.txt","r") as datei:
        # numpy array erstellen um einfacher damit um zu gehen
    np_array = []
    zahler = 0
    for spalte in datei:
        zahler += 1
        neue_spalte = []
        for zahl in spalte:
            if zahl.endswith("\n"):
                continue
            neue_spalte.append(int(zahl))
        np_array.append(neue_spalte)
    np_array = np.array(np_array)


# zeile
#print(np_array[0])

# spalte
#print(np_array[:,0])

# wie viele spalten es insgesamt gibt
#print(zahler)

baum_zahler = 0 # gibt die aktuelle zeile an
sichtbar = 0 # gibt die alle sichtbaren bäume an
nicht_sichtbar = 0 # gibt alle nicht sichtbaren bäume an
stellen_zahler = 0 # zähler für die vertikalen spalten

nicht_sichtbar_rechts = False
nicht_sichtbar_links = False
nicht_sichtbar_oben = False
nicht_sichtbar_unten = False


for reihe in np_array:
    if baum_zahler == 0 or baum_zahler == zahler -1 :
        # baum ist sichtbar
        sichtbar += zahler
        baum_zahler += 1
        continue
    sichtbar +=1
    
    for baum in reihe:
        stellen_zahler +=1
        print(reihe)
        nicht_sichtbar_rechts = False
        nicht_sichtbar_links = False
        nicht_sichtbar_oben = False
        nicht_sichtbar_unten = False

        if stellen_zahler == 0 or stellen_zahler == zahler - 1:
            sichtbar +=1
            stellen_zahler +=1
        else:
            #linker baum
            aktuelle_stelle = stellen_zahler
            while aktuelle_stelle > 0:
                if reihe[aktuelle_stelle-1] >= baum:
                    print(f"Nicht sichtbar von links sollte sein {baum}")
                    nicht_sichtbar_links = True
                    break

                aktuelle_stelle -= 1
            

            # rechter baum
            aktuelle_stelle = stellen_zahler
            while aktuelle_stelle < zahler:
                
                #print(f"aktueller baum {reihe[aktuelle_stelle]}")
                #print(f"rechter baum {reihe[aktuelle_stelle+1]}")
                if reihe[aktuelle_stelle+1] >= baum:
                    print(f"Nicht sichtbar von rechts sollte sein {baum}")
                    nicht_sichtbar_rechts = True
                    break

                aktuelle_stelle += 1
                if aktuelle_stelle == zahler-1:
                    break
            



            if nicht_sichtbar_rechts and nicht_sichtbar_links:
                print("----------------------neuer nicht sichtbarer")
                nicht_sichtbar += 1
                
            
            print("neuer baum")



        baum_zahler += 1

    stellen_zahler = 0
    baum_zahler += 1
print(sichtbar)
print(nicht_sichtbar)
