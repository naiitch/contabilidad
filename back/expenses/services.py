from db.connection import get_connection

def add_expense(user_id, category_id, amount, date, note):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO expenses (user_id, category_id, amount, date, note)
        VALUES (%s, %s, %s, %s, %s)
    """, (user_id, category_id, amount, date, note))

    conn.commit()
    cursor.close()
    conn.close()
