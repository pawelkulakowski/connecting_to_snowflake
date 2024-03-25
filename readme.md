
# Getting data from Snowflake to Pandas using three methods:

Method 1: using sqlalchemy snowflake connector

Method 2: using snowflake connector with fetch_pandas_all()

Method 3: using snowflake connector with fetch_pandas_betches()

The goal was to test three types of connections to get the data from snowflake for further data manipulation.

# Sample App

Created app is connecting to snowflake using snowflake.connector, creates new database, schema, table and insert new rows to the table. 