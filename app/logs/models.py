from db import get_db_connection

def insert_log(message):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (message) VALUES (%s);", (message,))
    conn.commit()
    cursor.close()
    conn.close()
