# Eine Datei schreiben
f = open("datei.txt", "wt")
f.write("Hallo\n")
f.write("Welt\n")
f.close()


# Datei einlesen und ausgeben
f = open("datei.txt", "rt")
for zeile in f:
    print(zeile, end="")
f.close()

# Datei einlesen und automatisch schließen
with open("datei.txt", "rt") as f:
    for zeile in f:
        print(zeile, end="")
