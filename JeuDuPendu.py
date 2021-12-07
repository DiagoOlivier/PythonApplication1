
# TODO: Mettre en place les lettres déja proposées
#  Aller chercher sur internet les mots --> Fait
# TODO: proposer la la longueur du mot au joueur
# TODO: mettre en place une IHM graphique
# TODO: ajouter un compteur
# TODO: afficher plus de texte
import RessourcesJeuduPendu as Re
longueurMot = 0
while longueurMot < 4 or longueurMot > 11:
    try:
        longueurMot = int(input("Avec quelle longueur de mot vous voulez jouer ? (entre 5 et 10)"))
        break
    except ValueError:
        print("Veuillez taper un nombre")
motATrouver = Re.motATrouver(longueurMot)
lettreProposee = ""
lettresDejaProposees = []
motTrouve = list("-" * len(motATrouver))
jeuEnCours = True
# Coeur du jeu
print(f"{Re.bcolors.OK}Jeu du pendu{Re.bcolors.RESET}")
print("Jeu du pendu")
while jeuEnCours:
    reponseIncorrecte = True
    while reponseIncorrecte:
        if len(lettresDejaProposees) != 0:
            print(f'Vous avez déjà proposé les lettres suivantes {" ".join(sorted(lettresDejaProposees))}')
        lettreProposee = input("Choisit une lettre : ")
        if len(lettreProposee) == 1 and 96 < ord(lettreProposee.lower()) < 123:
            lettreProposee = lettreProposee.lower()
            if lettresDejaProposees.count(lettreProposee) != 0:
                print(f'{Re.bcolors.WARNING}Désolé {lettreProposee} a déja été proposé !!!!{Re.bcolors.RESET}')
            else:
                lettresDejaProposees.append(lettreProposee)
                reponseIncorrecte = False

    if motATrouver.count(lettreProposee) != 0:
        print(f'Bravo {lettreProposee} fait partie du mot recherché')
        position = [i for i in range(len(motATrouver)) if motATrouver.startswith(lettreProposee, i)]
        for i in position:
            motTrouve[i] = lettreProposee
    else:
        print(f'Désolé mais {lettreProposee} ne fait pas partie du mot recherché')
    print(f'Debug {"".join(motTrouve)}')
    if motTrouve.count("-") == 0:
        jeuEnCours = False

print(f'Debug {"".join(motTrouve)}')
