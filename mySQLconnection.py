import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'jith123',
    port = '3306',
    database = 'atm-machine'
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM usersdb')

usersdb = mycursor.fetchall()

for user in usersdb:
    print(user)
