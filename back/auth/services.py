from db.connection import get_connection
from utils.auth import hash_password, check_password

def register_user(username, email, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
        (username, email, hash_password(password))
    )

    conn.commit()
    cursor.close()
    conn.close()

def login_user(email, password):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE email = %s",
        (email,)
    )

    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user and check_password(password, user["password_hash"]):
        return user

    return None
