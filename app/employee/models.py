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

def fetch_employees(page: int, limit: int, search: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Tính toán chỉ số bắt đầu
    start = (page - 1) * limit

    # Truy vấn với LIMIT, OFFSET và tìm kiếm
    query = """
        SELECT * FROM employees 
        WHERE name ILIKE %s 
        ORDER BY id  -- Sắp xếp theo ID hoặc một trường khác nếu cần
        LIMIT %s OFFSET %s;
    """
    cursor.execute(query, ('%' + search + '%', limit, start))
    records = cursor.fetchall()

    # Lấy tổng số bản ghi phù hợp với tìm kiếm
    count_query = "SELECT COUNT(*) FROM employees WHERE name ILIKE %s;"
    cursor.execute(count_query, ('%' + search + '%',))
    total_records = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return records, total_records

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
