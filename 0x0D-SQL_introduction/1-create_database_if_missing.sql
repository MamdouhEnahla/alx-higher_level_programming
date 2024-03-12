import mysql.connector

def create_database(database_name):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password"
        )

        cursor = connection.cursor()

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

        print(f"Database '{database_name}' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

create_database("hbtn_0c_0")
