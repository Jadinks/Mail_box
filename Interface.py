from ConnectionMailServer import *
import sqlite3


def choice_email(conn):
    cur = conn.cursor()
    cur.execute("SELECT address FROM email")
    rows = cur.fetchall()
    print("liste des emails :")
    listemail = []
    for r in rows:
        print(r[0])
        listemail.append(r[0])

    choice = input("veuillez entrer le nom de l'email que vous voulez ouvrir : ")
    validation = False
    while validation == False:
        if choice in listemail:
            validation = True
        elif choice == "0":
            return None
        else:
            choice = input("l'email choisi n'existe pas, veuillez en rechoisir un :")

    cur.execute("SELECT id FROM email WHERE address = '%s'" % choice)
    id = cur.fetchone()
    return int(id[0])


if __name__ == '__main__':
    conn = create_connection("pythonsqlite.db")

    id = choice_email(conn)
    print(id)
