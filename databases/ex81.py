import sqlalchemy as db

engine = db.create_engine("mysql+pymysql://root:root@localhost/testprog")

connection = engine.connect()

metadata = db.MetaData()

product = db.Table('product', metadata, autoload=True, autoload_with=engine)

product.drop(engine)