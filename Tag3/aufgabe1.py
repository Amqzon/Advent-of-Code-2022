with open("Tag3/rucksack.txt","r") as datei:
    alle_doppelten = []
    for i in datei:
        
        # split in two compartments
        h = int((len(i[:-1])+1)/2)
        abteil_eins = i[0:h]
        abteil_zwei = i[h:]

        for item in abteil_eins:
            if item in abteil_zwei:
                doppelt = item
            else:
                pass
        alle_doppelten.append(doppelt)
    # score ausrechnen
    werte = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    score = 0
    for i in alle_doppelten:
        score += werte.index(i)+1
    print(score)



