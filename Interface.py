from ConnectionMailServer import *
import sqlite3
from Read_mails import *


def choice():
    print("options :")
    print("a : send mail")
    print("b : synchro mail")
    print("c : local")
    print("d : Quit")
    choice = input("Please choose an option : ")
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
        if choice == 'd':
            return
        else:
            choice = input("Please choose an option : ")


def choice_send_mail():
    print("options :")
    print("a : send by outlook")
    print("b : send by gmail")
    print("c : Return")
    choice = input("Please choose an option : ")
    validation = False
    while validation == False:
        if choice == 'a':
            validation = True
            address = input("Enter your mail address :")
            password = input("Enter your password :")
            receiver = input("To :")
            subject = input("Subject :")
            email_text = input("Enter your text :")
            test = send_outlook(address,password,receiver,email_text,subject)
            if test != None:
                print (test)
        if choice == 'b':
            validation = True
            address = input("Enter your mail address :")
            password = input("Enter your password :")
            receiver = input("To :")
            subject = input("Subject :")
            email_text = input("Enter your text :")
            test = send_gmail(address, password, receiver, email_text, subject)
            if test != None:
                print(test)
        if choice == 'c':
            return
        else:
            choice = input("Please choose an option : ")
    choice_send_mail()


def choice_synchro_mail():
    print("options :")
    print("a : synchro outlook")
    print("b : synchro gmail")
    print("c : Return")
    choice = input("Please choose an option : ")
    validation = False
    while validation == False:
        if choice == 'a':
            validation = True
            address = input("Enter your email address")
            password = input("Enter you password")
            test = recup_dataoutlook(address,password)
            if test != None:
                print(test)
        if choice == 'b':
            validation = True
            address = input("Enter your email address")
            password = input("Enter you password")
            test = recup_datagmail(address, password)
            if test != None:
                print(test)
        if choice == 'c':
            return
        else:
            choice = input("Please choose an option : ")
    choice_synchro_mail()


def choice_local():
    print("options :")
    print("a : Check your mails")
    print("b : Check logs")
    print("c : Save mails on a file")
    print("d : Return")
    choice = input("Please choose an option : ")
    validation = False
    while validation == False:
        if choice == 'a':
            validation = True
            read_mails()
        if choice == 'b':
            validation = True
            conn = create_connection("pythonsqlite.db")
            print(select_log(conn))
        if choice == 'c':
            validation = True
            conn = create_connection("pythonsqlite.db")
            mail_to_file(conn)
            print("Fait")
        if choice == 'd':
            return
        else:
            choice = input("Please choose an option : ")
    choice_local()

if __name__ == '__main__':
    conn = create_connection("pythonsqlite.db")

    choice()
