# coding: utf-8
import imaplib
import email
import smtplib
from SQL_retriever import *

def recup_datagmail(mail:str,password:str):
    imap = imaplib.IMAP4_SSL('imap.gmail.com')
    imap.login(mail,password)
    (status, res) = imap.list()
    # renvoie ('OK', ['nombre de messages']) ou sinon ('NO', ['message erreur'])
    (status, numberMessages) = imap.select('INBOX')
    print(status, 'Nombre de messages = ', numberMessages)
    # renvoie par exemple ('OK', ['1 2 3 4 5']) qui sont les numéros des messages.
    (status, searchRes) = imap.uid("search",None, 'ALL')
    # Récupération des numéros des messages
    ids = searchRes[0].split()
    for i in range(len(ids)):
        # Récupère seulement l'expéditeur et le sujet dans le header
        (status, res) = imap.fetch(ids[i], '(BODY[HEADER.FIELDS (FROM SUBJECT TO DATE)])')
        for responsePart in res:
            if isinstance(responsePart, tuple):
                msg = email.message_from_bytes(responsePart[1])
                sender = str(email.header.make_header(email.header.decode_header(msg['From'])))
                subject = str(email.header.make_header(email.header.decode_header(msg['Subject'])))
                receiver = str(email.header.make_header(email.header.decode_header(msg['To'])))
                date = str(email.header.make_header(email.header.decode_header(msg['Date'])))
                print(receiver)
                print(date)
                print('expediteur : ', sender)
                print('sujet : ', subject)
    imap.close()
    imap.logout()


def recup_dataoutlook(mail:str,password:str):
    imap = imaplib.IMAP4_SSL('outlook.office365.com')
    imap.login(mail,password)
    (status, res) = imap.list()
    # renvoie ('OK', ['nombre de messages']) ou sinon ('NO', ['message erreur'])
    (status, numberMessages) = imap.select('INBOX')
    print(status, 'Nombre de messages = ', numberMessages)
    # renvoie par exemple ('OK', ['1 2 3 4 5']) qui sont les numéros des messages.
    (status, searchRes) = imap.uid("search",None, 'ALL')
    # Récupération des numéros des messages
    ids = searchRes[0].split()
    for i in range(len(ids)):
        # Récupère seulement l'expéditeur et le sujet dans le header
        (status, res) = imap.uid('fetch', ids[i], '(BODY.PEEK[HEADER])')
        for responsePart in res:
            if isinstance(responsePart, tuple):
                try:
                    msg = email.message_from_bytes(responsePart[1])
                    sender = str(email.header.make_header(email.header.decode_header(msg['From'])))
                    subject = str(email.header.make_header(email.header.decode_header(msg['Subject'])))
                    receiver = str(email.header.make_header(email.header.decode_header(msg['To'])))
                    date = str(email.header.make_header(email.header.decode_header(msg['Date'])))
                    print(receiver)
                    print(date)
                    print('expediteur : ', sender)
                    print('sujet : ', subject)
                except:
                    print("wrong mail")
    imap.close()
    imap.logout()

def send_outlook(user, password,receiver,email_text,subject):
    try:
        email_text = "Subject: " + subject + "\n\n" + email_text
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.ehlo()
        server.starttls()
        server.login(user,password)
        server.sendmail(user,receiver,email_text)
        server.close()
    except Exception as e:
        print(e)

def send_gmail(user, password,receiver,email_text,subject):
    try:
        email_text = "Subject: " + subject + "\n\n" + email_text
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(user,password)
        server.sendmail(user,receiver,email_text)
        server.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    #recup_datagmail('projetiosnetwork@gmail.com','projectisfun')
    #recup_dataoutlook('projetiosnetwork@outlook.fr','projectisfunOutlook')
    subject = 'OMG Super Important Message'
    body = "Hey, what'sup? - You"
    #send_gmail('projetiosnetwork@gmail.com','projectisfun','projetiosnetwork@outlook.fr',body,'OMG Super Important Message')
    #send_outlook('projetiosnetwork@outlook.fr','projectisfunOutlook','projetiosnetwork@gmail.com',body,'OMG Super Important Message !')