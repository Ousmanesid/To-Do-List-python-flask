import sqlite3

def get_db_connection():
    conn = sqlite3.connect('taches.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with sqlite3.connect('taches.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS taches")
        cursor.execute("""
        CREATE TABLE taches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            description TEXT NOT NULL,
            date TIMESTAMP DEFAULT (strftime('%Y-%m-%d %H:%M', 'now'))
        )
        """)
        conn.commit()

def get_all_tasks():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM taches').fetchall()
    conn.close()
    return tasks

def add_task(titre, description):
    conn = get_db_connection()
    conn.execute('INSERT INTO taches (titre, description) VALUES (?, ?)', (titre, description))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM taches WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
