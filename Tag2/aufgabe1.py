with open("Tag2/game_plan.txt", "r") as datei:
    score = 0
    for i in datei:
        zuege = i.split(" ")
        if len(zuege[1]) > 1 :
            zuege[1] = zuege[1][0]
        # check for win condition
        # rock vs paper 
        if (zuege[0] == "A") and (zuege[1] == "Y"):
            score += 2 + 6
            
        # rock vs scissors
        elif (zuege[0] == "A") and (zuege[1] == "Z"):
            score += 3 + 0

        # paper vs scissors
        elif (zuege[0] == "B") and (zuege[1] == "Z"):
            score += 3 + 6
        # paper vs rock
        elif (zuege[0] == "B") and (zuege[1] == "X"):
            score += 1 + 0

        # scissors vs paper
        elif (zuege[0] == "C") and (zuege[1] == "Y"):
            score += 2 + 0 
        # scissors vs rock
        elif (zuege[0] == "C") and (zuege[1] == "X"):
            score += 1 + 6

        # draw
        else:
            score += 3
            if zuege[1] == "X":
                score += 1
            elif zuege[1] == "Y":
                score += 2
            elif zuege[1] == "Z":
                score += 3
        print(score)
    print(score)
