import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)



def main():
    database = r"D:\Network Architecture\Projet\Mail_box\pythonsqlite.db"
    
    sql_create_email_table = """ CREATE TABLE IF NOT EXISTS email (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        address text NOT NULL,
                                        password text NOT NULL,
                                        service text NOT NULL); """
    
    sql_create_mail_table = """CREATE TABLE IF NOT EXISTS mail (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        sender text NOT NULL, 
                                        receiver text NOT NULL,
                                        body text NOT NULL, 
                                        date text NOT NULL, 
                                        subject text NOT NULL,
                                        email_id integer NOT NULL,
                                        FOREIGN KEY (email_id) REFERENCES email (id));"""
    
    sql_create_log_table = """ CREATE TABLE IF NOT EXISTS log (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        type text NOT NULL,
                                        ip text NOT NULL,
                                        date text NOT NULL,
                                        service text NOT NULL); """
     
    conn = create_connection(database)
    
    if conn is not None:
        create_table(conn, sql_create_email_table)
        create_table(conn, sql_create_mail_table)
        create_table(conn, sql_create_log_table)
    else:
        print("Error! cannot create the database connection.")
        
if __name__ == '__main__':
    main()