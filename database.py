import mysql.connector
from datetime import datetime

config = {
    'user': 'service007',
    'password': 'language007',
    'host': 'db4free.net',
    'database': 'service007',
}


def seup_database():
    config['database'] = None
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        email VARCHAR(255),
        username VARCHAR(255),
        password VARCHAR(255),
        is_admin BOOLEAN
    )
""")
