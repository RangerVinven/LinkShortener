import mysql.connector
import MySQLdb.cursors.DictCursor

connection = mysql.connector.connect(user="link", password="password",
                              host="linkshortener-db-1",
                              database="LinkShortener",
                              cursorclass=MySQLdb.cursors.DictCursor)
cursor = connection.cursor()
