import sqlalchemy as db
import pandas as pd

engine = db.create_engine("mysql+pymysql://root:root@localhost/testprog")

connection = engine.connect()

metadata = db.MetaData()

emp = db.Table('emp', metadata, autoload=True, autoload_with=engine)

metadata.create_all(engine)

#Inserting many records at ones
query = db.insert(emp) 
values_list = [{'Id':'2', 'name':'ram', 'salary':80000, 'active':False},
               {'Id':'3', 'name':'ramesh', 'salary':70000, 'active':True},
               {'Id':'4', 'name':'naveen', 'salary':90000, 'active':True}]
ResultProxy = connection.execute(query,values_list)

results = connection.execute(db.select([emp])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
print(df.head(4))
