import sqlite3

# You can see the DB manually throw the DB Browser for SQLite
# https://sqliteonline.com


# Simulates a connection to the DB
connection = sqlite3.connect('fotocasa.db')
cursor = connection.cursor()

# Executes the query to create a table
cursor.execute("""
               create table fotocasa_tb(
                   text text,
                   author text,
                   url_author text,
                   tags text
               )
               """)

# Executes the query to create the table and closes the connection
connection.commit()
connection.close()
