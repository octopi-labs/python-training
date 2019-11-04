import sqlalchemy as db

engine = db.create_engine("mysql+pymysql://root:root@localhost/testprog")

connection = engine.connect()

metadata = db.MetaData()

product = db.Table('product', metadata, autoload=True, autoload_with=engine)

# SELECT id, name, price FROM product WHERE category_id IN (1, 2)
query = db.select([product.columns.id, product.columns.name, 
            product.columns.price]).where(product.columns.category_id.in_([1, 2]))

result = connection.execute(query).fetchall()

print(result)
