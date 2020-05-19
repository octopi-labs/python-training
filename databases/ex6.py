import sqlalchemy as db

engine = db.create_engine("mysql+pymysql://root:root@localhost/testprog")

connection = engine.connect()

metadata = db.MetaData()

product = db.Table('product', metadata, autoload=True, autoload_with=engine)

query = db.select([product])

ResultProxy = connection.execute(query)

flag = True

while flag:
    partial_results = ResultProxy.fetchmany(50)
    print(partial_results)
    flag = (partial_results != [])

ResultProxy.close()

