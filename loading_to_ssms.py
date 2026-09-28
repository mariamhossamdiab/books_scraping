import pandas as pd
import pyodbc
#print(pyodbc.drivers())
# Make connection to SQL Server
connection = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    r"SERVER=localhost\SQLEXPRESS;"
    "DATABASE=test;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

cursor = connection.cursor()

# Read the CSV file
df = pd.read_csv("books.csv")

# Create table in SQL Server
create_table_query = """
CREATE TABLE books (
    title VARCHAR(255),
    price FLOAT,
    rating INT,
    in_stock BIT,
    url VARCHAR(500)
)
"""

cursor.execute(create_table_query)
connection.commit()

# Insert rows from DataFrame into SQL Server
insert_query = """
INSERT INTO test.dbo.books (
    title,
    price,
    rating,
    in_stock,
    url
)
VALUES (?, ?, ?, ?, ?)
"""

for row in df.itertuples(index=False):
    cursor.execute(
        insert_query,
        (
            row.title,
            row.price,
            row.rating,
            row.in_stock,
            row.url
        )
    )

connection.commit()

cursor.close()
connection.close()

print("Data loaded successfully!")