from sqlalchemy import create_engine
import pandas as pd

df = pd.read_excel("Online Retail.xlsx")

engine = create_engine("sqlite:///online_retail.sqlite")
df.to_sql("retail", con=engine)
print("It's done")