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

    print(path_dict)

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
        continue
    else:
        pfad_kurz = pfad.split("/")
        pfad_fuer_filesystem = pfad_kurz[len(pfad_kurz)-1]
        print(pfad_fuer_filesystem)

        filesystem[pfad_fuer_filesystem] = zahler
        zahlen_wert.append(zahler)
        zahler = 0
print(filesystem)
print(zahlen_wert)

# alle zahlen die kleiner als 10.000 sind zusammen rechnen
ergebnis = 0
for i in zahlen_wert:
    if i <= 100000:
        ergebnis += i
print(ergebnis)