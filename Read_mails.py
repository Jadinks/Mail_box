from numpy import *
from SQL_retriever import *


def read_emails():
     indice_list = display_mails()
     mail_number = input("Which mail do you want to open ? 0 to go back : ")
     if input == 0:
         return
     read_email(mail_number)
     read_emails()

def display_mails():
    conn = create_connection("pythonsqlite.db")
    rows = select_subject_sender_mail(conn)
    i = 1
    for row in rows :
        subject = row.split("'")[1]
        sender = row.split("'")[3]
        print (i,":", subject,"Sender : ", sender)
        i+=1
    return

def read_email(mail_number):
    return
