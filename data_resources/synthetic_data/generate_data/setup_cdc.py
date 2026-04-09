"""this script is used to enable Change Tracking at both the database and table level,
allowing SQL Server to monitor changes such as inserts, updates, and deletes.
This is a one-time configuration step that prepares the database for incremental processing.
This capability is essential because it allows downstream processes to identify only what has changed since the last update,
rather than scanning entire tables. In a production environment,
this significantly improves efficiency and forms the backbone of any incremental data pipeline.
"""




import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()

server_name = os.getenv("SERVER_NAME")
username = os.getenv("SERVER_ADMIN_LOGIN")
database = os.getenv("DATABASE_USERNAME")
password = os.getenv("DATABASE_PASSWORD")

conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={server_name};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    "TrustServerCertificate=yes;",
    autocommit=True
)

cursor = conn.cursor()

SCHEMA = "dbo"

TABLES = [
    "customers",
    "historical_orders",
    "menu_items",
    "restaurants",
    "customer_reviews"
]

#  Enable Change Tracking at DB level
cursor.execute(f"""
IF NOT EXISTS (
    SELECT 1 FROM sys.change_tracking_databases 
    WHERE database_id = DB_ID('{database}')
)
BEGIN
    ALTER DATABASE [{database}]
    SET CHANGE_TRACKING = ON
    (CHANGE_RETENTION = 14 DAYS, AUTO_CLEANUP = ON);
END
""")
conn.commit()

#  Enable Change Tracking on tables
for table in TABLES:
    cursor.execute(f"""
    IF NOT EXISTS (
        SELECT 1 
        FROM sys.change_tracking_tables
        WHERE object_id = OBJECT_ID('{SCHEMA}.{table}')
    )
    BEGIN
        ALTER TABLE [{SCHEMA}].[{table}]
        ENABLE CHANGE_TRACKING
        WITH (TRACK_COLUMNS_UPDATED = ON);
    END
    """)
    conn.commit()

print(" Change Tracking enabled successfully.")

cursor.close()
conn.close()