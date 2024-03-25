import pandas as pd
import snowflake.connector
from datetime import datetime

# method 2 using fetch_pandas_all() 
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

start_time = datetime.now()
cur.execute(query)
df = cur.fetch_pandas_all()

cur.close()

end_time = datetime.now()
total_time = end_time - start_time
print(df)
print(f'Duration time: {total_time}')

