with open("./Tag1/elfen_kalorien.txt","r") as datei:
    Maximal_kalorien = 0
    aktuelle_kalorien = 0
    alle_elfen = []
    for i in datei:
        if i == "\n":
            # Neuer elfe
            alle_elfen.append(aktuelle_kalorien)
            aktuelle_kalorien = 0
            continue
        else:
            
            aktuelle_kalorien = aktuelle_kalorien + int(i)
    
    sortiert = sorted(alle_elfen,reverse=True)
    print(sortiert)
    # die top 3 zusammen gerechnet
    top3 = sortiert[0] + sortiert[1] + sortiert[2]
    print(top3)
