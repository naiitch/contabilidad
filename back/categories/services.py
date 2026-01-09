from db.connection import get_connection

def create_category(user_id, name, type_):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO categories (user_id, name, type)
        VALUES (%s, %s, %s)
    """, (user_id, name, type_))

    conn.commit()
    cursor.close()
    conn.close()
