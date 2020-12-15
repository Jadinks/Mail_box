# coding: utf-8
import imaplib
import email


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


if __name__ == "__main__":
    recup_datagmail('projetiosnetwork@gmail.com','projectisfun')
