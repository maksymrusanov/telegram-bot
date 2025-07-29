import sqlite3
from pathlib import Path
DB_PATH = Path(__file__).parent/'db'/'db.sqlite3'


def get_rows(page: int = 0, page_size: int = 10):
    conn = sqlite3.connect(DB_PATH)
    curr = conn.cursor()
    offset = page * page_size
    curr.execute('SELECT * FROM offers LIMIT ? OFFSET ?', (page_size, offset))
    rows = curr.fetchall()
    curr.close()
    conn.close()
    return rows
