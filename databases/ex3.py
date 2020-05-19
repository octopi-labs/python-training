# importing the module
import pymysql
# import pymssql as pymysql

try:
    # opening a database connection
    conn = pymysql.connect("localhost", "root", "root", "testprog", autocommit=True)

    # define a cursor object
    cursor = conn.cursor()

    # SQL query string
    sqlQuery = "SELECT firstname, lastname, id FROM employee"   

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