import snowflake.connector
import pandas as pd

conn = snowflake.connector.connect(
    user='xxx',
    password='xxx',
    account='xxx',
    warehouse='COMPUTE_WH',
    role='ACCOUNTADMIN'
    )

# creating database, schema, table and inserting values

conn.cursor().execute("CREATE DATABASE IF NOT EXISTS testdb")
conn.cursor().execute("USE DATABASE testdb")
conn.cursor().execute("CREATE SCHEMA IF NOT EXISTS testschema")
conn.cursor().execute("USE SCHEMA testschema")
conn.cursor().execute(
    "CREATE OR REPLACE TABLE "
    "test_table(col1 integer, col2 string)")
conn.cursor().execute(
    "INSERT INTO test_table(col1, col2) "
    "VALUES(123, 'test string1'),(456, 'test string2')")

# getting data from database in snowflake

# fetch one
col1, col2 = conn.cursor().execute("SELECT col1, col2 FROM test_table").fetchone()
print('{0}, {1}'.format(col1, col2))

# print all rows
for (col1, col2) in conn.cursor().execute("SELECT col1, col2 FROM test_table"):
	print('{0}, {1}'.format(col1, col2))

# converting sql query to dataframe
df = conn.cursor().execute("SELECT * FROM test_table").fetch_pandas_all()

conn.close()
print(df)
