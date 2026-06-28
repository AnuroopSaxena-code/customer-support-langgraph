import sqlite3

DB_NAME = "memory.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS conversations(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        conversation_id TEXT,
        customer_name TEXT,
        query TEXT,
        response TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_memory(conversation_id, customer_name, query, response):

    conn = sqlite3.connect(DB_NAME)

    conn.execute(
        """
        INSERT INTO conversations
        (conversation_id, customer_name, query, response)
        VALUES(?,?,?,?)
        """,
        (
            conversation_id,
            customer_name,
            query,
            response
        )
    )

    conn.commit()
    conn.close()


def recall_last_issue(conversation_id):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.execute(
        """
        SELECT query
        FROM conversations
        WHERE conversation_id=?
        ORDER BY id DESC
        LIMIT 2
        """,
        (conversation_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    if len(rows) < 2:
        return "No previous support issue found."

    return rows[1][0]


init_db()
