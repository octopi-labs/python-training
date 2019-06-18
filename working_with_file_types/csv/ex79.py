# importing csv module
import pandas
import os

current_dir = os.path.dirname(__file__)
# csv file name
filename = os.path.join(current_dir, "test_1.csv")

df = pandas.read_csv(filename, index_col='Name')
print(df)
