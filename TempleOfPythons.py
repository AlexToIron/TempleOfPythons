# Importation de la bibliothèque "random"
import random

# Création d'un espace vide pour espacer les sorties console
space = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

# Affichage du titre du jeu
print("\nTemple of Pythons")

# Message d'accueil pour les joueurs
print("\nBienvenua au temple des python, \navancez dans le temple en choisissant la bonne porte, \nmais si vous choisissez la mauvaise porte les Pythons vont vous attaquer et vous aurez perdu !")

# Saut de ligne pour l'affichage
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

# Affichage du menu avec deux options : jouer ou quitter
menu = int(input("1) Jouer \n2) Quitter \n"))

# Vérification de l'entrée de l'utilisateur pour le menu
while menu not in [1, 2]:
    menu = int(input("1) Jouer \n2) Quitter \n"))

# Si l'utilisateur a choisi de jouer, le jeu commence et le paramètre "run" est défini sur True.
if menu == 1:
    run = True
    print(space)

# Si l'utilisateur a choisi de quitter, le programme se termine avec la fonction "exit ()".
if menu == 2:
    exit()

# Initialisation du score et du niveau
score = 0

level = 1

# Définition d'une bonne porte aléatoire entre 1 et 4
GoodDoor = random.randint(1, 4)

# Affichage d'un message pour expliquer la situation du joueur
print("\nVous explorez un temple perdu au fond de la jungle du Python, \nVous entrez dedans et découvrez que pour acceder à la salle du trésor vous devez passer par plusieurs portes mais vous ne savez pas laquelle de ses portes et la bonne, \n")

# Boucle while qui se poursuit tant que le joueur ne perd pas
while run:
    # Sélection aléatoire d'une nouvelle bonne porte pour chaque niveau
    GoodDoor = random.randint(1, 4)
    # Affichage de la bonne porte choisie pour le niveau actuel (pour le débogage)
    # print(GoodDoor)
    # Demande à l'utilisateur de choisir une porte
    choiceDoor = int(input("\nChoisissez la bonne porte pour accéder à la salle suivante. \n1) Porte une\n2) Porte deux \n3) Porte trois \n4) Porte quatre : "))
    # Vérification de l'entrée de l'utilisateur pour la sélection de porte
    while choiceDoor not in [1, 2, 3, 4]:
        choiceDoor = int(input("\nLe nombre doit etre entre 1 et 4 \nChoisissez la bonne porte pour accéder à la salle suivante. \n1) Porte une\n2) Porte deux \n3) Porte trois \n4) Porte quatre : "))
    # Condition quand le joueur choisi la bonne porte 
    if choiceDoor == GoodDoor:
        level += 1
        score += 1
        print(f"\nFélicitation vous avez choisi la bonne porte, vous etes maintenant dans la salle {level}, \nvotre score : {score}")
    # Condition quand il choisi la mauvaise porte
    else:
        run = False
        print("Oh non ! Un python vous a attaqué ! Vous avez perdu...")
        print(f"Votre score : {score} \nVous étiez au niveau : {level}")
        restart = input("Voulez-vous recommencer ? (o/n)")
        if restart == "n":
            run = False
        elif restart == "o":
            print(space)
            # Initialisation du score et du niveau
            score = 0

            level = 1

            # Définition d'une bonne porte aléatoire entre 1 et 4
            GoodDoor = random.randint(1, 4)

            # Affichage d'un message pour expliquer la situation du joueur
            print("\nVous explorez un temple perdu au fond de la jungle du Python, \nVous entrez dedans et découvrez que pour acceder à la salle du trésor vous devez passer par plusieurs portes mais vous ne savez pas laquelle de ses portes et la bonne, \n")
            run = True
