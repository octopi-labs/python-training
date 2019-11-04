import sqlalchemy as db

engine = db.create_engine("mysql+pymysql://root:root@localhost/testprog")

connection = engine.connect()

metadata = db.MetaData()

# Create a table
emp = db.Table('emp', metadata,
                db.Column('Id', db.Integer()),
                db.Column('name', db.String(200), nullable=False),
                db.Column('salary', db.Float(), nullable=False, default=100.00),
                db.Column('active', db.Boolean(), default=True)
            )

metadata.create_all(engine)

# Insert single record
query = db.insert(emp).values(Id=1, name='Rahul', salary=60000.00, active=True) 
ResultProxy = connection.execute(query)
