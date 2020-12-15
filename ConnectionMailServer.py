# coding: utf-8
import imaplib
import email
import smtplib
from SQL_retriever import all

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


def send_gmail(user, password,receiver,email_text,subject):
    try:
        email_text = """\
            From: %s
            To: %s
            Subject: %s

            %s
            """ % ('projetiosnetwork@gmail.com', ", ".join('alexis.ledoux29@gmail.com'), subject, email_text)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(user,password)
        server.sendmail(user, receiver, email_text)
        server.close()
        # ...send emails
    except:
        print('Something went wrong...')


if __name__ == "__main__":
    recup_datagmail('projetiosnetwork@gmail.com','projectisfun')
    subject = 'OMG Super Important Message'
    body = "Hey, what'sup?\n\n - You"
    send_gmail('projetiosnetwork@gmail.com','projectisfun','alexis.ledoux29@gmail.com',body,
               'OMG Super Important Message')

    conn = create_connection("pythonsqlite.db")
    if conn is not None:
        insert_email(conn, (1, "addresse1", "password1", "service1"))
        insert_mail(conn, (40000, "sender1", "receiver1", "body1", "date1", "subject1", 1))

        conn.close()
    else:
        print("Error! cannot create the database connection.")