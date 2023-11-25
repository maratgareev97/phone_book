import connect


def createTable(nameTable):
    con = connect.connection()
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS " + nameTable + " (id int NOT NULL AUTO_INCREMENT, name text, phone text, description text, PRIMARY KEY (id));")
    con.commit()

    cur.close()
    con.close()


def getAllData():
    con = connect.connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM test_table;")
    result = cur.fetchall()  # в виде строки

    cur.close()
    con.close()
    return result


def addNewData(name, phone, description):
    con = connect.connection()
    cur = con.cursor()
    cur.execute("""insert into test_table(name, phone, description) VALUES (%s,%s,%s)""",
                (name, phone, description))
    con.commit()

    cur.close()
    con.close()


def deleteById(id):
    con = connect.connection()
    cur = con.cursor()
    cur.execute("""DELETE FROM test_table WHERE id=%s""", (id))
    con.commit()

    cur.close()
    con.close()

def getDataById(id):
    con = connect.connection()
    cur = con.cursor()
    cur.execute("""SELECT id, name, phone, description FROM test_table WHERE id = %s""", (id))
    result = cur.fetchall()

    cur.close()
    con.close()
    return result


def updateDataById(id, name, phone, description):
    con = connect.connection()
    cur = con.cursor()
    cur.execute("""UPDATE test_table SET name=%s, phone=%s, description=%s WHERE id=%s""",
                (name, phone, description, id))
    con.commit()

    cur.close()
    con.close()
