import mysql.connector

con = mysql.connector.connect(
    host ="localhost",
    user = "root",
    passwd = "",

)

if con.is_connected():
    print("koneksi ke server database ok!")

db = con.cursor()
db.execute("create database db_akademik_0341")