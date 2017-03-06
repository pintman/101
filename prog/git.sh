# Shell-Befehle für die Arbeit mit git

#  Leeres Repo im akt. Verz. erstellen
git init

# Repo von Server kopieren
git clone git@server:/pfad

# Unterschiede zeigen
git diff

# Letzte Änderungen
git log -p

# Dateien vormerken
git add datei.txt

# Änderungen in Repo speichern  
git commit

# Ext. Repo konfigurieren
git remote add

# Änderungen hochladen
git push

# Branch erstellen
git checkout -b branchname

# Branch zusammenführen
git merge <branch>

# Branch löschen
git branch -d <branch>

# Git-Server einrichten
# - User git anlegen: adduser git
# - Public Keys in Datei /home/git/.ssh/authorized_keys speichern.
# - Repo für Projekt anlegen: sudo git init –-bare /opt/git/projekt.git
# - ggf. Rechte anpassen: sudo chown -R git:git /opt/git/projekt.git
