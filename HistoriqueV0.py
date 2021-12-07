import sys
import pathlib
import sqlite3
import collections
try:
    Dossier = pathlib.Path(sys.argv[1])
except IndexError:
    sys.exit("Il faut un chemin de profi")
historique = Dossier / "places.sqlite"
if not historique.is_file:
    print("Ce n'est pas un fichier")
connexion = sqlite3.connect(str(historique))
curseur = connexion.cursor()
requete =""" 
SELECT moz_places.rev_host 
FROM moz_historyvisits,moz_places 
where moz_places.id = moz_historyvisits.id
"""
resultat = curseur.execute(requete)

g = (l[0][-2:-1].replace("www","") for l in resultat)
compteur = collections.Counter(g)
#print(compteur.most_common(10))
print("DEbug : OK")
for site,nombre in compteur.most_common(10):
    print("_ ",site," : ",nombre)