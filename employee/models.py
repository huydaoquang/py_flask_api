import psycopg2
from db import get_db_connection

def fetch_all_employees():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees;")
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records

def add_employee(name, salary):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO employees (name, salary) VALUES (%s, %s) RETURNING id;",
        (name, salary)
    )
    employee_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return employee_id

def update_employee(id, name, salary):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE employees SET name = %s, salary = %s WHERE id = %s;",
        (name, salary, id)
    )
    conn.commit()
    cursor.close()
    conn.close()

def delete_employee(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id = %s;", (id,))
    conn.commit()
    cursor.close()
    conn.close()
