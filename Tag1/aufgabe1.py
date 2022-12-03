with open("./Tag1/elfen_kalorien.txt","r") as datei:
    Maximal_kalorien = 0
    aktuelle_kalorien = 0
    for i in datei:
        if i == "\n":
            # Neuer elfe
            if aktuelle_kalorien >= Maximal_kalorien:
                Maximal_kalorien = aktuelle_kalorien
            aktuelle_kalorien = 0
            continue
        else:
            
            aktuelle_kalorien = aktuelle_kalorien + int(i)
    print(Maximal_kalorien)

