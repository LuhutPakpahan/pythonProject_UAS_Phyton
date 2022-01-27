import mysql.connector

con = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  db = "db_akademik_0341"

)

dbcursor = con.cursor()
sql = "select * from tbl_students_0341"
dbcursor.execute(sql)
dt = dbcursor.fetchall()

for data in dt:
  print(data)