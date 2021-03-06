# coding: utf-8
import imaplib
import email
import smtplib
from SQL_retriever import *

def recup_datagmail(mail:str,password:str):
    imap = imaplib.IMAP4_SSL('imap.gmail.com')
    try:
        imap.login(mail,password)
    except Exception as e:
        return e
    conn = create_connection("pythonsqlite.db")
    if not email_exist(conn,mail):
        insert_email(conn,(mail,password,"gmail"))
    (status, res) = imap.list()
    # renvoie ('OK', ['nombre de messages']) ou sinon ('NO', ['message erreur'])
    (status, numberMessages) = imap.select('INBOX')
    print(status, 'Nombre de messages = ', numberMessages)
    # renvoie par exemple ('OK', ['1 2 3 4 5']) qui sont les numéros des messages.
    (status, searchRes) = imap.uid("search",None, 'ALL')
    # Récupération des numéros des messages
    ids = searchRes[0].split()

    id = select_id_email(conn,mail)
    drop_mail(conn,id[0])
    for i in range(len(ids)):
        # Récupère seulement l'expéditeur et le sujet dans le header
        (status, res) = imap.uid('fetch', ids[i], '(RFC822)')
        for responsePart in res:
            if isinstance(responsePart, tuple):
                msg = email.message_from_bytes(responsePart[1])
                sender = str(email.header.make_header(email.header.decode_header(msg['From'])))
                subject = str(email.header.make_header(email.header.decode_header(msg['Subject'])))
                receiver = str(email.header.make_header(email.header.decode_header(msg['To'])))
                date = str(email.header.make_header(email.header.decode_header(msg['Date'])))
                body = msg.get_payload()
                mail = (sender,receiver,body,date,subject,id[0])
                insert_mail(conn,mail)
    imap.close()
    imap.logout()
    update_log("gmail", "sync")


def recup_dataoutlook(mail:str,password:str):
    imap = imaplib.IMAP4_SSL('outlook.office365.com')
    try:
        imap.login(mail,password)
    except Exception as e:
        return e
    conn = create_connection("pythonsqlite.db")
    if not email_exist(conn, mail):
        insert_email(conn, (mail, password, "outlook"))
    (status, res) = imap.list()
    # renvoie ('OK', ['nombre de messages']) ou sinon ('NO', ['message erreur'])
    (status, numberMessages) = imap.select('INBOX')
    print(status, 'Nombre de messages = ', numberMessages)
    # renvoie par exemple ('OK', ['1 2 3 4 5']) qui sont les numéros des messages.
    (status, searchRes) = imap.uid("search",None, 'ALL')
    # Récupération des numéros des messages
    ids = searchRes[0].split()
    id = select_id_email(conn, mail)
    drop_mail(conn, id[0])
    for i in range(len(ids)):
        # Récupère seulement l'expéditeur et le sujet dans le header
        (status, res) = imap.uid('fetch', ids[i], '(RFC822)')
        for responsePart in res:
            if isinstance(responsePart, tuple):
                try:
                    msg = email.message_from_bytes(responsePart[1])
                    sender = str(email.header.make_header(email.header.decode_header(msg['From'])))
                    subject = str(email.header.make_header(email.header.decode_header(msg['Subject'])))
                    receiver = str(email.header.make_header(email.header.decode_header(msg['To'])))
                    date = str(email.header.make_header(email.header.decode_header(msg['Date'])))
                    body = msg.get_payload()
                    mail = (sender, receiver, body, date, subject, id[0])
                    insert_mail(conn, mail)
                except:
                    print("wrong mail")
    imap.close()
    imap.logout()
    update_log("outlook", "sync")

def send_outlook(user, password,receiver,email_text,subject):
    try:
        email_text = "To: " + receiver + "\nSubject: " + subject + "\n\n" + email_text
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.ehlo()
        server.starttls()
        server.login(user,password)
        server.sendmail(user,receiver,email_text)
        server.close()
        update_log("outlook", "send")
    except Exception as e:
        return e

def send_gmail(user, password,receiver,email_text,subject):
    try:
        email_text = "To: " + receiver + "\nSubject: " + subject + "\n\n" + email_text
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(user,password)
        server.sendmail(user,receiver,email_text)
        server.close()
        update_log("gmail", "send")
    except Exception as e:
        return e


if __name__ == "__main__":
    conn = create_connection("pythonsqlite.db")
    #drop_all_mail(conn)
    #drop_email(conn)
    #drop_log(conn)
    #recup_datagmail('projetiosnetwork@gmail.com','projectisfun')
    #recup_dataoutlook('projetiosnetwork@outlook.fr','projectisfunOutlook')
    subject = 'OMG Super Important Message'
    body = "I'm not crazy ?? Are you sure ? - You"
    #send_gmail('projetiosnetwork@gmail.com','projectisfun','projetiosnetwork@outlook.fr',body,'OMG Super Important Message')
    #send_outlook('projetiosnetwork@outlook.fr','projectisfunOutlook','projetiosnetwork@gmail.com',body,'OMG!')
    print(select_all_email(conn))
    print(select_log(conn))
    #mail_to_file(conn)
    input()