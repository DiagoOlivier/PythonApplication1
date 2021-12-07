import random
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLORs



class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def motATrouver(n):
    motConforme = False
    listeMots = open('liste_francais.txt')
    l = listeMots.read(228239).split("\n")
    while motConforme == False:
        mot = l[int(random.random()*len(l))]
        if len(mot) != n:
            motConforme = False
        elif mot.istitle() or lettreAccentue(mot):
            motConforme = False
        else:
            motConforme = True
    listeMots = ""
    return mot


def lettreAccentue(mot):
    for i in mot:
        if ord(i.lower()) < 96 or ord(i.lower()) > 123:
            return True
    return False





