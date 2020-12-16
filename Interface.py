from ConnectionMailServer import *


def choice_email():
    choice = input("veuillez entrer l'email que vous voulez ouvrir : ")
    validation = False
    while validation == False:
        if choice == "email":
            return choice
        else:
            choice = input("l'email choisi n'existe pas, veuillez en rechoisir un :")