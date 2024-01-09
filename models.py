import mysql.connector
from database import config
from mysql.connector import Error


class User():
    def __init__(self, id, first_name, last_name, username, email, password, is_admin=False):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password_hash = password
        self.username = username
        self.is_admin = is_admin
        

    @classmethod
    def get(cls, user_id):
        pass


def add_user(first_name, last_name, email, username, password, is_admin=False):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        query = "INSERT INTO users (first_name, last_name, username, email, password, is_admin) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (first_name, last_name, username, email, password, is_admin))
        connection.commit()
    except mysql.connector.Error as err:
        print("Error: ", err)
    finally:
        cursor.close()
        connection.close()
    return True


def get_user_by_email(email):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        if user:
            return User(*user)
    except mysql.connector.Error as err:
        print("Error: ", err)
    finally:
        cursor.close()
        connection.close()
    return None



def get_user_by_username(username):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        if user:
            return User(*user)
    except mysql.connector.Error as err:
        print("Error: ", err)