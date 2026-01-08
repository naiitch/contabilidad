from db.connection import get_connection

def create_budget(user_id, category_id, amount, period, start_date):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO budgets (user_id, category_id, amount, period, start_date)
        VALUES (%s, %s, %s, %s, %s)
    """, (user_id, category_id, amount, period, start_date))

    conn.commit()
    cursor.close()
    conn.close()


def get_budgets(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT b.*, c.name AS category
        FROM budgets b
        LEFT JOIN categories c ON b.category_id = c.id
        WHERE b.user_id = %s
    """, (user_id,))

    budgets = cursor.fetchall()
    cursor.close()
    conn.close()

    return budgets
