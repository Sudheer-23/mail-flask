import mysql.connector as c
con = c.connect(host = "localhost",user = "root",password = "sudheer123",database = "nsrit")
def show1():
    cursor = con.cursor()
    cursor.execute("""select email from sqldb1;""")
    table1 = cursor.fetchall()
    l = list(table1)
    con.commit()
    cursor.close()
    print(l)
    return l


def showResult(per):
    cursor = con.cursor()
    cursor.execute("""select * from students where id between {per} and 4;""".format(per=per))
    table = cursor.fetchall()
    con.commit()
    cursor.close()
    return table

#cursor.execute(""" select * from sqldb2 where Percentage between {per} and 75.00;""".format(per =per))