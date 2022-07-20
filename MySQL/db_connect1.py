import mysql.connector as mysql
from mysql.connector import Error


def connect():
    # connect of MySQL DB
    # this is method 1 to connect mysql db.
    # but this method is risky. try method 2.
    conn = None
    try:
        conn = mysql.connect(host='localhost',
                             database='python_mysql',
                             user='root',
                             password='!@#$')
        if conn.is_connected():
            print("Successfully connected with database")

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()
