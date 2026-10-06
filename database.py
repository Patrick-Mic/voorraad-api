import sqlite3

DB_PATH = "voorraad.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS producten (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                naam TEXT NOT NULL,
                aantal INTEGER NOT NULL DEFAULT 1,
                houdbaar_tot TEXT,
                toegevoegd_op TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)