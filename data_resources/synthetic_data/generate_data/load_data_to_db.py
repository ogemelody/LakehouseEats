import pyodbc
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
server_name = os.getenv("SERVER_NAME")
username = os.getenv("SERVER_ADMIN_LOGIN")
database= os.getenv("DATABASE_USERNAME")
password = os.getenv("DATABASE_PASSWORD")

#print(server_name, database, username, password)

conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={server_name};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    "TrustServerCertificate=yes;"
)



cursor = conn.cursor()


def load_csv_to_table(cursor, conn, csv_path, table_name):
    df = pd.read_csv(csv_path)

    df = df.where(pd.notnull(df), None)

    # Build CREATE TABLE statement from column names
    columns = ", ".join([f"[{col}] NVARCHAR(255)" for col in df.columns])
    cursor.execute(f"DROP TABLE IF EXISTS [{table_name}]")
    cursor.execute(f"CREATE TABLE [{table_name}] ({columns})")
    conn.commit()

    # Insert rows
    placeholders = ", ".join(["?" for _ in df.columns])
    insert_sql = f"INSERT INTO [{table_name}] VALUES ({placeholders})"

    for _, row in df.iterrows():
        cursor.execute(insert_sql, tuple(row))

    conn.commit()
    print(f"✅ Loaded {len(df)} rows into [{table_name}]")


# --- Define your 3 CSVs and table names here ---

script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.abspath(os.path.join(script_dir, "..", "data"))

files = [(os.path.join(data_dir, "menu_items.csv"), "menu_items"),
          (os.path.join(data_dir, "customers.csv"), "customers"),
          (os.path.join(data_dir, "orders.csv"), "orders")]


for csv_path, table_name in files:
    load_csv_to_table(cursor, conn, csv_path, table_name)



conn.commit()
cursor.close()
conn.close()