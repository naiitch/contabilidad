from db.connection import get_connection

def get_user_profile(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, username, email, created_at
        FROM users
        WHERE id = %s
    """, (user_id,))

    user = cursor.fetchone()
    cursor.close()
    conn.close()

    return user


def update_user_profile(user_id, username, email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET username = %s, email = %s
        WHERE id = %s
    """, (username, email, user_id))

    conn.commit()
    cursor.close()
    conn.close()


def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM users WHERE id = %s",
        (user_id,)
    )

    conn.commit()
    cursor.close()
    conn.close()
