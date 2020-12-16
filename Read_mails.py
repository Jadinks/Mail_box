from numpy import *
from SQL_retriever import *


def read_mails():
     liste_ids = display_mails()
     mail_number = "a"
     while not mail_number.isnumeric():
        mail_number = input("Which mail do you want to open ? 0 to go back : ")
     if mail_number == '0':
         return
     read_mail(int(mail_number),liste_ids)
     read_mails()

def display_mails():
    choix_order = -1
    conn = create_connection("pythonsqlite.db")
    while(choix_order not in ['1','2','3','4']):
        choix_order = input("Choose the ordering parameter : Date (1), Sender (2), Receiver (3), Subject (4).")
        if choix_order == '1' :
            rows = select_mail(conn)
        elif choix_order == '2' :
            rows = select_mail_order_sender(conn)
        elif choix_order == '3' :
            rows = select_mail_order_receiver(conn)
        elif choix_order == '4' :
            rows = select_mail_order_subject(conn)
    ids = []
    i=1
    for row in rows :
        sender = row[1]
        receiver = row[2]
        subject = row[5]
        print (i,":","From : ", sender, "To : ", receiver, "Subject : ", subject)
        i += 1
        ids.append(row[0])
    return ids

def read_mail(mail_number,liste_ids):
    conn = create_connection("pythonsqlite.db")
    mail= select_one_mail(conn,liste_ids[mail_number-1])
    mail = mail[0]
    print("From :", mail[1], "To", mail[2])
    print("Date : ",mail[4])
    print("Subject : ", mail[5])
    print(mail[3])
    input("Press any key to go back")
    return

if __name__ == "__main__":
    read_mails()
