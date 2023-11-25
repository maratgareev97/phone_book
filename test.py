import pymysql
def con():
    connection = pymysql.connect(host='82.146.35.88',
                                 user='school',
                                 password='Q1w2e3r4',
                                 db='school',
                                 charset='cp1251',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

def cret():
    connection=con()
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS table2 (id int NOT NULL AUTO_INCREMENT, name text, phone text, description text, PRIMARY KEY (id));")
    connection.commit()
    cursor.close()
    connection.close()

def ins():
    connection=con()

    cursor = connection.cursor()
    cursor.execute("insert into table2 (name, phone, description) VALUES (1,2,3)")
    connection.commit()
    cursor.close()
    connection.close()

def sel():
    connection=con()


    cursor = connection.cursor()
    cursor.execute("SELECT * FROM table2")
    result = cursor.fetchall()  # в виде строки
    cursor.close()
    connection.close()
    for i in result:
        print(i)

cret()
ins()
sel()



