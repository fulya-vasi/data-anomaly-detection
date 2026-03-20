import sqlite3

def save_to_sqlite(df, db_path="data/anomaly_data.db", table_name="sensor_data"):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

