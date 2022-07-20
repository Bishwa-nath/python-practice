from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def connect():
    # connect of MySQL DB
    # this is method 2.
    # don't use database information directly
    db_config = read_db_config()
    conn = None
    try:
        print('Connection to MySQL Database...')
        conn = MySQLConnection(**db_config)
        if conn.is_connected():
            print("Database connected successfully.")
        else:
            print("Connection failed!")

    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("Connection closed.")


if __name__ == '__main__':
    connect()
