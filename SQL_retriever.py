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
        return c
    except Error as e:
        print(e)


def show_result(cur):
    rows = cur.fetchall()
    for r in rows:
        print(r)


def insert_mail(conn, project):
    """ Create a new project into the projects table """
    sql = ''' INSERT INTO mail(id,sender,receiver,body,date,subject)
              VALUES(?,?,?,?,?,?) '''
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


def select_mail_group_by(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM mail GROUP BY Nom")

    rows = cur.fetchall()
    for r in rows:
        print(r)




