import sqlalchemy as db

engine = db.create_engine("mysql+pymysql://root:root@localhost/testprog")

connection = engine.connect()

metadata = db.MetaData()

product = db.Table('product', metadata, autoload=True, autoload_with=engine)

# SELECT * FROM product WHERE id = 1
query = db.select([product]).where(product.columns.id == 1)

result = connection.execute(query).fetchall()

print(result)
