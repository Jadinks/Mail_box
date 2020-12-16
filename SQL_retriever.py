import sqlite3
from sqlite3 import Error
from datetime import datetime
import socket

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)


def execute_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement """
    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
        return cur
    except Error as e:
        print(e)

#################### DROP EVERYTHING ###############################

def drop_email(conn):
    sql = 'DELETE FROM email'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def drop_log(conn):
    sql = 'DELETE FROM log'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def drop_mail(conn, email_id):
    sql = 'DELETE FROM mail WHERE email_id=?'
    cur = conn.cursor()
    cur.execute(sql, (email_id,))
    conn.commit()
    return cur.lastrowid

def drop_all_mail(conn):
    sql = 'DELETE FROM mail'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

##################################################################

def select_id_email(conn, nom):
    cur = conn.cursor()
    cur.execute("SELECT id FROM email WHERE address = '%s'" % nom)
    id = cur.fetchone()
    print(id)
    return id

def email_exist(conn, nom):
    res = False
    nom = (nom,)
    cur = conn.cursor()
    cur.execute("SELECT address FROM email WHERE address='%s'" % nom)
    rows = cur.fetchall()
    for r in rows:
        if (r == nom):
            res = True
    return res

####################### INSERT INTO DB ###########################

def insert_email(conn, project):
    """ Create a new project into the projects table """
    sql = ''' INSERT INTO email(address,password,service)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def insert_mail(conn, project):
    """ Create a new project into the projects table """
    sql = ''' INSERT INTO mail(sender, receiver, body, date, subject, email_id)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def insert_log(conn, project):
    """ Create a new project into the projects table """
    sql = ''' INSERT INTO log(type,ip,date,service)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

##################################################################

###################### SELECT EVERYTHING FROM DB #################
def select_all_email(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM email")
    rows = cur.fetchall()
    # print(rows)
    return rows

def select_log(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM log")
    rows = cur.fetchall()
   # print(rows)
    return rows

def select_mail(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM mail")
    rows = cur.fetchall()
#    for r in rows:
#        print(r)
    return(rows)

###################################################################

########################## 6)   SORTING EMAILS ####################

def select_mail_order_sender(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM mail ORDER BY sender")
    rows = cur.fetchall()
#    for r in rows:
#        print(r)
    return(rows)

def select_mail_order_receiver(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM mail ORDER BY receiver")
    rows = cur.fetchall()
#    for r in rows:
#        print(r)
    return(rows)
        

def select_mail_order_subject(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM mail ORDER BY subject")
    rows = cur.fetchall()
#    for r in rows:
#        print(r)
    return(rows)

####################################################################

##################### 8)  SAVING EMAILS TO A FILE ##################

def mail_to_file(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM mail")
    rows = cur.fetchall()
    fichier = open("mail.txt", "w")
    for r in rows:
        fichier.write("\n")
        fichier.write(str(r))
    fichier.close()

####################################################################    
    
###################### 7)   UPDATE LOG   ###########################

def update_log(service, obj):
    conn = create_connection("pythonsqlite.db")
    
    date = datetime.now()
    ip = socket.gethostbyname(socket.gethostname())
    sql = ''' INSERT INTO log(type,ip,date,service)
              VALUES(?,?,?,?) '''
    data_tuple = (obj, str(ip), str(date), service)
    cur = conn.cursor()
    cur.execute(sql, data_tuple)
    conn.commit()
    return cur

#####################################################################        



if __name__ == '__main__':
    conn = create_connection("pythonsqlite.db")
    
    #email = ('projetiosnetwork@gmail.com','projectisfun',"gmail")
    
    #bis = ('projetiosnetwork@outlook.fr','projectisfunOutlook',"outlook")

    #insert_email(conn, bis)
    #select_id_email(conn, 'projetiosnetwork@outlook.fr')
    
    
    #mail = ('projettwork@outlook.fr','projetiosnetwork@gmail.com','ghgjb', 'date', 'sagvabgné', 1)
    
    #insert_mail(conn,mail)
    
    #select_mail(conn)
    
    #select_mail_order_subject(conn)
    
    #select_all_email(conn)

    #drop_email(conn)
    
    #drop_mail(conn, 1)
    
    #drop_log(conn)
    
    #update_log("gmail", "login")
    #select_log(conn)

    
    #mail_to_file(conn)

    #print(email_exist(conn, 'projetiosnetwork@outlook.fr'))
    
    
    
    
    
    