import mysql.connector

connection = mysql.connector.connect(user="link", password="password",
                              host="linkshortener-db-1",
                              database="LinkShortener")
cursor = connection.cursor(dictionary=True)
