import sqlite3
import pandas as pd

df = pd.read_csv("seoul/seoul_data.csv", encoding="UTF-8")
conn = sqlite3.connect("seoul.db")

df.to_sql("seoul_market", conn, if_exists="replace", index=False)

conn.close()
