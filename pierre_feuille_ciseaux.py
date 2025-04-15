import random

options = ["pierre", "ciseaux", "feuille"]
selection_rand = random.choice(options)

choix = input("Choisissez Pierre, Feuille ou Ciseaux: ")

if choix in options:
    if choix == selection_rand:
        print("Egalité")
    else:
        if (choix == "pierre" and selection_rand == "ciseaux") \
            or (choix == "feuille" and selection_rand == "pierre") \
                or (choix == "ciseaux" and selection_rand == "feuille"):
            print("Bravo, vous avez gagné")
        else:
            print("Vous avez perdu")

    print("Choix de l'ordinateur :", selection_rand)
else:
    print("Choix incorrect: options - pierre, feuille, ciseaux")
