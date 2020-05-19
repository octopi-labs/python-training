import sqlalchemy as db

engine = db.create_engine("mysql+pymysql://root:root@localhost/testprog")

connection = engine.connect()

metadata = db.MetaData()

product = db.Table('product', metadata, autoload=True, autoload_with=engine)

query = db.select([product])

ResultProxy = connection.execute(query)

ResultSet = ResultProxy.fetchall()

print(ResultSet)