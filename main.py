import mysql.connector



db = mysql.connector.connect(
    host ="localhost",
    user = "root",
    passwd = "",
    database = "db_akademik_0341"

)


def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM tbl_students_0341"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)


def search_data(db):
    cursor = db.cursor()
    keyword = input("Kata kunci: ")
    sql = "SELECT * FROM tbl_students_0341 WHERE nim LIKE %s"
    val = ("%{}%".format(keyword))
    cursor.execute(sql, val)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)

def search_data_limit(db):
    cursor = db.cursor()
    keyword = input("Kata kunci: ")
    sql = "SELECT * FROM tbl_students_0341"
    val = ("%{}%".format(keyword))
    cursor.execute(sql, val)
    results = cursor.fetchmany(val)

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)


def show_menu(db):
    print("=== APLIKASI DATABASE PYTHON ===")
    print("1. Tampilkan Data")
    print("2. Tampilan berdasar limit")
    print("3. Pencarian Berdasar NIM")
    print("4. Pencarian Berdasar LIMIT")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih menu> ")


    if menu == "1":
        show_data(db)
    elif menu == "2":
        insert_data(db)
    elif menu == "3":
        search_data(db)
    elif menu == "4":
        search_data_limit(db)
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")


if __name__ == "__main__":
    while(True):
        show_menu(db)