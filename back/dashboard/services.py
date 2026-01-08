from db.connection import get_connection

def get_balance(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
        (SELECT IFNULL(SUM(amount),0) FROM incomes WHERE user_id=%s) -
        (SELECT IFNULL(SUM(amount),0) FROM expenses WHERE user_id=%s)
    """, (user_id, user_id))

    balance = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    return balance
