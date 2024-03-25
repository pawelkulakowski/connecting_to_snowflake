
import pandas as pd
import snowflake.connector
from datetime import datetime

# method 3 using fetch_pandas_batches() 
# pip install "snowflake-connector-python[pandas]"

conn = snowflake.connector.connect(
    user='xxx',
    password='xxx',
    account='xxx',
    warehouse='COMPUTE_WH',
    database='GARDEN_PLANTS',
    schema='VEGGIES',
    role='ACCOUNTADMIN'
)

cur = conn.cursor()

query = "SELECT * FROM lu_soil_type"
batches=[]

start_time = datetime.now()
cur.execute(query)
for df in cur.fetch_pandas_batches():
    batches.append(df)

df = pd.concat(batches, ignore_index=True)


cur.close()

end_time = datetime.now()
total_time = end_time - start_time
print(df)
print(f'Duration time: {total_time}')