import sqlalchemy as db
import pandas as pd

engine = db.create_engine("mysql+pymysql://root:root@localhost/testprog")

connection = engine.connect()

metadata = db.MetaData()

product = db.Table('product', metadata, autoload=True, autoload_with=engine)

category = db.Table('category', metadata, autoload=True, autoload_with=engine)

# Manual Join
query = db.select([product, category])
query = query.select_from(product.join(category, product.columns.category_id == category.columns.id))

result = connection.execute(query).fetchall()

df = pd.DataFrame(result)

df.columns = result[0].keys()

print(df.head(20))