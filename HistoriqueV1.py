import sys
import pathlib
import sqlite3
import collections
from tkinter import Tk,Frame, Text, filedialog, messagebox, END

app = Tk()
app.title('Sistes visités')
fenetre = Frame(app)
zoneTexte = Text (fenetre, height = 20, width = 40)
zoneTexte.pack()
fenetre.pack()
dossierProfil = filedialog.askdirectory()
if not dossierProfil:
    sys.exit(0)


historique = pathlib.Path (dossierProfil) / "places.sqlite"
if not historique.is_file:
    messagebox.showwarning("Ce n'est pas un fichier")
    sys.exit(0)
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
#print("DEbug : OK")
for site,nombre in compteur.most_common(10):
    ligne = site  + " : " + str(nombre) + " visite \n"
    zoneTexte.insert(END,ligne)
app.mainloop()
