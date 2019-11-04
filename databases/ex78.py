import sqlalchemy as db
import pandas as pd

engine = db.create_engine("mysql+pymysql://root:root@localhost/testprog")

connection = engine.connect()

metadata = db.MetaData()

emp = db.Table('emp', metadata, autoload=True, autoload_with=engine)

results = connection.execute(db.select([emp])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
print(df.head(4))

# Build a statement to update the salary to 100000
query = db.update(emp).values(salary = 100000)
query = query.where(emp.columns.Id == 1)
results = connection.execute(query)

results = connection.execute(db.select([emp])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
print(df.head(4))
