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


def show_result(cur):
    rows = cur.fetchall()
    for r in rows:
        print(r)


def select_id_email(conn, nom):
    cur = conn.cursor()
    cur.execute("SELECT id FROM email WHERE email = '%s'" % nom)
    id = cur.fetchone()
    return id


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
    sql = ''' INSERT INTO mail(sender,receiver,body,date,subject,email_id)
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


def select_all_mail(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM mail")
    rows = cur.fetchall()
    return rows


def drop_mail(conn, email_id):
    sql = 'DELETE FROM mail WHERE email_id=?'
    cur = conn.cursor()
    cur.execute(sql, email_id)
    conn.commit()
    return cur.lastrowid

##### 3)   RETRIEVING EMAILS

def select_mail(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM mail")
    rows = cur.fetchall()
    for r in rows:
        print(r)

##### 6)   SORTING EMAILS

def select_mail_group_sender(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM mail GROUP BY sender")
    rows = cur.fetchall()
    for r in rows:
        print(r)

def select_mail_group_receiver(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM mail GROUP BY receiver")
    rows = cur.fetchall()
    for r in rows:
        print(r)

def select_mail_group_subject(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM mail GROUP BY subject")
    rows = cur.fetchall()
    for r in rows:
        print(r)

##### 8)  SAVING EMAILS TO A FILE 

def email_to_file(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM mail")
    rows = cur.fetchall()
    fichier = open("mail.txt", "a")
    for r in rows:
        fichier.write("\n"+r)
    fichier.close()
    
##### 7)   UPDATE LOG

def update_log(service, obj):
    conn = create_connection("pythonsqlite.db")
    
    date = datetime.date
    ip = socket.gethostbyname(socket.gethostname())
    sql = ''' INSERT INTO log(type,ip,date,service)
              VALUES(?,?,?,?) '''
    data_tuple = (obj, ip, date, service)
    try:
        cur = conn.cursor()
        cur.execute(sql, data_tuple)
        return cur
    except Error as e:
        print(e)

#fuck mathis#        
