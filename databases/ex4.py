import sqlalchemy as db

## Connecting to the database
## engine = db.create_engine('dialect+driver://user:pass@host:port/db')

engine = db.create_engine("mysql+pymysql://root:root@localhost/testprog")

connection = engine.connect()

metadata = db.MetaData()

product = db.Table('product', metadata, autoload=True, autoload_with=engine)

print(product.columns.keys())

print(repr(metadata.tables['product']))

