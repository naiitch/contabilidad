from db.connection import get_connection

def expenses_by_category(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT c.name AS category, SUM(e.amount) AS total
        FROM expenses e
        JOIN categories c ON e.category_id = c.id
        WHERE e.user_id = %s
        GROUP BY c.name
    """, (user_id,))

    result = cursor.fetchall()
    cursor.close()
    conn.close()

    return result


def expenses_over_time(user_id, year, month=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if month:
        cursor.execute("""
            SELECT DATE(date) as day, SUM(amount) as total
            FROM expenses
            WHERE user_id = %s AND YEAR(date) = %s AND MONTH(date) = %s
            GROUP BY DATE(date)
        """, (user_id, year, month))
    else:
        cursor.execute("""
            SELECT MONTH(date) as month, SUM(amount) as total
            FROM expenses
            WHERE user_id = %s AND YEAR(date) = %s
            GROUP BY MONTH(date)
        """, (user_id, year))

    result = cursor.fetchall()
    cursor.close()
    conn.close()

    return result
