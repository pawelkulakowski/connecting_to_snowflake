import pandas as pd
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL
from datetime import datetime

# method 1 using sqlalchemy 
# pip install --upgrade snowflake-sqlalchemy

url = URL(
    account = 'xxx',
    user = 'xxx',
    password = 'xxx',
    database = 'GARDEN_PLANTS',
    schema = 'VEGGIES',
    warehouse ='COMPUTE_WH',
    role ='ACCOUNTADMIN'
)

engine = create_engine(url)

connection = engine.connect()
query = "SELECT * FROM lu_soil_type"
start_time = datetime.now()

df = pd.read_sql(query, connection)
end_time = datetime.now()
connection.close()
total_time = end_time - start_time

print(df)
print(f'Duration time: {total_time}')