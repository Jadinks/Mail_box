# coding: utf-8
import imaplib
import email
imap = imaplib.IMAP4_SSL('imap.gmail.com')
imap.login('projetiosnetwork@gmail.com','projectisfun')
(status, res) = imap.list()
# renvoie ('OK', ['nombre de messages']) ou sinon ('NO', ['message erreur'])
(status, numberMessages) = imap.select('INBOX')
print(status, 'Nombre de messages = ', numberMessages)
# renvoie par exemple ('OK', ['1 2 3 4 5']) qui sont les numéros des messages.
(status, searchRes) = imap.search(None, 'ALL')
# Récupération des numéros des messages
ids = searchRes[0].split()
for i in range(len(ids)):
    # Récupère seulement l'expéditeur et le sujet dans le header
    (status, res) = imap.fetch(ids[i], '(BODY[HEADER.FIELDS (FROM SUBJECT)])')
    for responsePart in res:
        if isinstance(responsePart, tuple):
            response = responsePart[1]
            msg = email.message_from_bytes(response)
            sender = msg['from'].encode("ASCII").decode("utf-8")
            subject = msg['subject'].encode("ASCII").decode("utf-8")
            print('expediteur : ', sender)
            print('sujet : ', subject)
imap.close()
imap.logout()
