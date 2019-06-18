# importing the module
import pymysql
# import pymssql as pymysql


try:
    # opening a database connection
    conn = pymysql.connect("localhost", "root", "root", "testprog", autocommit=True)

    # define a cursor object
    cursor = conn.cursor()

    # query
    sql = "INSERT INTO employee2(id, lastname, firstname, departmentcode) VALUES(2, 'Shelke', 'Rahul1', '254')"

    # execute query
    cursor.execute(sql)

    # commit the changes
    conn.commit()
    cursor.close()
except Exception as e:
    print("Exeception occured:{}".format(e))
finally:
    # close connection
    conn.close()