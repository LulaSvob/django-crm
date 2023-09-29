import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost', 
    user = 'root', 
    passwd = '3@ns$cv3z%4&PPRf',
    auth_plugin='mysql_native_password'
    
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")