from db.connection import get_connection

def add_income(user_id, category_id, amount, date, description):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO incomes (user_id, category_id, amount, date, description)
        VALUES (%s, %s, %s, %s, %s)
    """, (user_id, category_id, amount, date, description))

    conn.commit()
    cursor.close()
    conn.close()
