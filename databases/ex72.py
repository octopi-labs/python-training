import sqlalchemy as db

engine = db.create_engine("mysql+pymysql://root:root@localhost/testprog")

connection = engine.connect()

metadata = db.MetaData()

product = db.Table('product', metadata, autoload=True, autoload_with=engine)

# SELECT SUM(price) FROM product
query = db.select([db.func.sum(product.columns.price)])

result = connection.execute(query).fetchall()

print(result)
