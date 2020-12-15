import sqlite3
from sqlite3 import Error


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


def insert_email(conn, project):
    """ Create a new project into the projects table """
    sql = ''' INSERT INTO email(id,address,password,service)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def insert_mail(conn, project):
    """ Create a new project into the projects table """
    sql = ''' INSERT INTO mail(id,sender,receiver,body,date,subject,email_id)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def insert_log(conn, project):
    """ Create a new project into the projects table """
    sql = ''' INSERT INTO log(id,login,ip,date,service)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def select_all_mail(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM mail")

    rows = cur.fetchall()
    for r in rows:
        print(r)


def select_mail_order_by(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM mail ORDER BY id ASC")

    rows = cur.fetchall()
    for r in rows:
        print(r)

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

if __name__ == "__main__":
    select_all_mail(create_connection("pythonsqlite.db"))