import bcrypt
from db import get_db_connection

def register_user(username, password):
    if not isinstance(username, str) or not isinstance(password, str):
        raise ValueError("Username and password must be strings")
    
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE username = %s;", (username,))
    if cursor.fetchone() is not None:
        cursor.close()
        conn.close()
        raise ValueError("Username already exists")
    
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s) RETURNING id;",
        (username, hashed_password.decode('utf-8')) 
    )
    
    user_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    
    return {
        "user_id":user_id,
        "username": username,
        "message": "User registered successfully",
        "status": 201
    }


def login_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT password FROM users WHERE username = %s;", (username,))
    record = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if record and bcrypt.checkpw(password.encode('utf-8'), record[0].encode('utf-8')):
        return True
    return False

def change_password(username, old_password, new_password):
    if not isinstance(username, str) or not isinstance(old_password, str) or not isinstance(new_password, str):
        raise ValueError("Username, old password, and new password must be strings")
    
    conn = get_db_connection()
    cursor = conn.cursor()

    # Kiểm tra xem username có tồn tại không
    cursor.execute("SELECT password FROM users WHERE username = %s;", (username,))
    result = cursor.fetchone()

    if result is None:
        cursor.close()
        conn.close()
        raise ValueError("Username does not exist")

    # Kiểm tra mật khẩu cũ
    stored_password = result[0].encode('utf-8')
    if not bcrypt.checkpw(old_password.encode('utf-8'), stored_password):
        cursor.close()
        conn.close()
        raise ValueError("Old password is incorrect")

    # Mã hóa mật khẩu mới
    hashed_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

    # Cập nhật mật khẩu mới
    cursor.execute(
        "UPDATE users SET password = %s WHERE username = %s;",
        (hashed_new_password.decode('utf-8'), username)
    )
    
    conn.commit()
    cursor.close()
    conn.close()

    return {
        "username": username,
        "message": "Password changed successfully",
        "status": 200
    }

def delete_user(username):
    if not isinstance(username, str):
        raise ValueError("Username must be a string")
    
    conn = get_db_connection()
    cursor = conn.cursor()

    # Kiểm tra xem username có tồn tại không
    cursor.execute("SELECT id FROM users WHERE username = %s;", (username,))
    result = cursor.fetchone()

    if result is None:
        cursor.close()
        conn.close()
        raise ValueError("Username does not exist")

    # Xóa người dùng
    cursor.execute("DELETE FROM users WHERE username = %s;", (username,))
    conn.commit()
    
    cursor.close()
    conn.close()

    return {
        "username": username,
        "message": "User deleted successfully",
        "status": 200
    }