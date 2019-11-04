# importing the module
import pymysql
# import pymssql as pymysql


try:
    # opening a database connection
    conn = pymysql.connect("localhost", "root", "root", "testprog", autocommit=True)

    # define a cursor object
    cursor = conn.cursor()

    # drop table if exists
    cursor.execute("DROP TABLE IF EXISTS employee;")

    # query
    sql = "CREATE TABLE employee(id int, lastname varchar(32), firstname varchar(32), departmentcode int) "

    # execute query
    cursor.execute(sql)

    # SQL query string
    sqlQuery = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_CATALOG='testprog'"  # "show tables"   

    # Execute the sqlQuery
    cursor.execute(sqlQuery)

    #Fetch all the rows
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Exception as e:
    print("Exeception occured:{}".format(e))
finally:
    cursor.close()

# close connection
conn.close()