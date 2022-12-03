with open("Tag3/rucksack.txt","r") as datei:
    alle_doppelten = []
    gruppe = []
    zahler = 0
    doppelt = ""

    for i in datei:
        gruppe.append(i[:-1])
        zahler += 1
        if zahler == 3:
            print(gruppe)
            zahler = 0
            for i in gruppe[0]:
                if (i in gruppe[1]) and (i in gruppe[2]):
                    print(i)
                    doppelt = i
            gruppe = []
        
            alle_doppelten.append(doppelt)
    # score ausrechnen
    werte = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    score = 0
    for i in alle_doppelten:
        score += werte.index(i)+1
    print(score)



