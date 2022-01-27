import mysql.connector

con = mysql.connector.connect(
    host ="localhost",
    user = "root",
    passwd = "",
    db = "db_akademik_0341"

)

if con.is_connected():
    print("koneksi ke database db_akademik_0341 ok!")

db = con.cursor()
db.execute("create table if not exists tbl_students_0341(id int(4), nim varchar(10), nama varchar(20),jk varchar(2), jurusan varchar(10), alamat varchar(50)) ")