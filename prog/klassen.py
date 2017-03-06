# Klasse für Person definieren
class Person:
    def __init__(self, name, alter=18):
        self.name = name
        self.alter = alter

    def altern(self):
        self.alter += 1

    def alter_erfragen(self):
        return self.alter
    
# Objekte aus der Klasse erzeugen
peter = Person("Peter")
petra = Person("Petra", alter=19)


# Klasse Schueler erbt von Klasse Person
class Schueler(Person):
    def __init__(self, name, klasse, alter=18):
        super().__init__(name, alter)
        self.klasse = klasse

max = Schueler("Max", "IT10")
