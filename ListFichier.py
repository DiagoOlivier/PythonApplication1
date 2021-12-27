import os

variable = 'var nom = new objet ("'
repertoire = input("Quel est le répertoire a scanner ?")
listFichier = os.listdir(repertoire)
listFichier = '","'.join(listFichier)
listFichier = 'var nom = new objet ("' + listFichier + '");'
print(listFichier)

