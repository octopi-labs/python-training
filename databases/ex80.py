import sqlalchemy as db

engine = db.create_engine("mysql+pymysql://root:root@localhost/testprog")

connection = engine.connect()

metadata = db.MetaData()

emp = db.Table('emp', metadata, autoload=True, autoload_with=engine)

# Drop emp table
emp.drop(engine)
