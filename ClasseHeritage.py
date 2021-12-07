class Identite:
    def __init__(self, nom, couleur):
        self.nom = nom
        self.couleur = couleur


class Animal:
    def __init__(self, espece, cri):
        self.espece = espece
        self.cri = cri

    def crier(self):
        print(self.cri)


class Humain(Animal):
    def __init__(self, nom, couleur, cri):
        self.espece = "humain"
        self.cri = cri
        self.Identite = Identite(nom, couleur)

    def crier(self):
        print("bonjour")
        super().crier()


#chien = Animal("Mamifére", "ouaf")
#chien.crier()
olivier = Humain("diago","rouge", "byyyyeu")
# olivier.crier()
print(olivier.Identite.couleur)
