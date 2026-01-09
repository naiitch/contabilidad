from db.connection import get_connection
import random

def get_random_message():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM messages")
    messages = cursor.fetchall()

    cursor.close()
    conn.close()

    if not messages:
        return None

    return random.choice(messages)
