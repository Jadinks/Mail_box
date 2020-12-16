from ConnectionMailServer import *
import sqlite3


def choice():
    print("options :")
    print("a = envoyer mail")
    print("b = synchro mail")
    print("c = local")
    choice = input("veuillez entrer l'option choisi : ")
    validation = False
    while validation == False:
        if choice == 'a':
            validation = True
            choice_send_mail()
        if choice == 'b':
            validation = True
            choice_synchro_mail()
        if choice == 'c':
            validation = True
            choice_local()
        else:
            choice = input("veuillez entrer une option disponible : ")


def choice_send_mail():
    print("options :")
    print("a = envoyer par outlook")
    print("b = envoyer par gmail")
    choice = input("veuillez entrer l'option choisi : ")
    validation = False
    while validation == False:
        if choice == 'a':
            validation = True

        if choice == 'b':
            validation = True

        else:
            choice = input("veuillez entrer une option disponible : ")


def choice_synchro_mail():
    print("options :")
    print("a = recup outlook")
    print("b = recup gmail")
    choice = input("veuillez entrer l'option choisi : ")
    validation = False
    while validation == False:
        if choice == 'a':
            validation = True

        if choice == 'b':
            validation = True

        else:
            choice = input("veuillez entrer une option disponible : ")


def choice_local():
    print("options :")
    print("a = voir tous les mails")
    print("b = trier les mails")
    print("c = voir les logs")
    print("d = recupérer les mails sur un fichier fait chier")
    choice = input("veuillez entrer l'option choisi : ")
    validation = False
    while validation == False:
        if choice == 'a':
            validation = True

        if choice == 'b':
            validation = True

        if choice == 'c':
            validation = True

        if choice == 'd':
            validation = True

        else:
            choice = input("veuillez entrer une option disponible : ")


if __name__ == '__main__':
    conn = create_connection("pythonsqlite.db")

    choice()
