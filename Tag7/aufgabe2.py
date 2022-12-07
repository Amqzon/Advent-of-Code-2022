with open("Tag7/aufgabe.txt","r") as datei:
    curren_path = ""
    path_dict = {}
    path_size = []
    file = False
    for command in datei:
        command = command[:-1]

        #check if line is a command
        if command.startswith("$"):
            file = False
            # for Path traversal
            if command == "$ cd ..":
                curren_path= curren_path.split("/")
                curren_path = curren_path[:-1]
                neu = "/"
                curren_path.pop(0)
                curren_path.pop(0)
                for i in curren_path:
                    neu = neu + "/" + i
                curren_path = neu
                continue
            elif command.startswith("$ cd "):
                curren_path = curren_path + "/" + command[5:]
            elif command == "$ ls":
                file = True
        else:
            try:
                path_dict[curren_path].append(command)
            except KeyError:
                path_dict[curren_path] = []
                path_dict[curren_path].append(command)



zahlen_wert = []
filesystem = {}
zahler = 0
neues_path_dict = {}
for k in sorted(path_dict, key=len, reverse=True):
    neues_path_dict[k] = path_dict[k]

path_dict = neues_path_dict

for pfad in path_dict:
    zahler = 0
    k = path_dict[pfad]
    for datei in k:
        if datei.startswith("dir "):
            if datei[4:] in filesystem:
                
                zahler += int(filesystem[datei[4:]])
            pass
        else:
            datei = datei.split(" ")
            zahler += int(datei[0])
    if pfad == "/":
        
        filesystem["/"] = zahler
        continue
    else:
        pfad_kurz = pfad.split("/")
        pfad_fuer_filesystem = pfad_kurz[len(pfad_kurz)-1]


        filesystem[pfad_fuer_filesystem] = zahler
        zahlen_wert.append(zahler)
        zahler = 0




path_dict2 = {}

for pfad in neues_path_dict:
    pfad_zum_sehen = pfad.split("/")
    pfad_zum_sehen.pop(0)
    pfad_zum_sehen.pop(0)
    
    #schauen wie groß der pfad ist und das dann ab speichern

    try:
        path_dict2[pfad] = filesystem[pfad_zum_sehen[-1]]
    except IndexError:
        continue

print(path_dict2)

#oberste pfade
top_path = {}




for pfad in neues_path_dict:
    pfad_zum_sehen = pfad.split("/")
    pfad_zum_sehen.pop(0)
    pfad_zum_sehen.pop(0)
    try:
        top_path[pfad_zum_sehen[0]] = filesystem[pfad_zum_sehen[0]]
    except IndexError:
        # pfad muss root sein
        pass

root_pfad = filesystem["/"]

# freier speicher
insgesamte_speicher = 70000000
mindestens_benoetigter_speicher = 30000000
ziel = insgesamte_speicher - mindestens_benoetigter_speicher

freier_speicher = insgesamte_speicher - root_pfad

belegte_speicher = insgesamte_speicher - freier_speicher
benoetigter_speicher = root_pfad - ziel




# die einzelnen pfade wenn einer davon gelöscht wird

moeglichkeiten = []
zahler = 0
for pfad in filesystem:
    #print(pfad + " " + str(filesystem[pfad]))
    danach_speicher = root_pfad - filesystem[pfad]
    
    if  filesystem[pfad] >=benoetigter_speicher:
        print(pfad + " " + str(filesystem[pfad]))
        moeglichkeiten.append(filesystem[pfad])
    else:
        continue


moeglichkeiten.sort()
print(moeglichkeiten)

# Dieser code funktioniert manchmal 