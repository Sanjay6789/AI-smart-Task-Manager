import sqlite3
from datetime import datetime

DB_PATH = "database/tasks.db"

def init_db():
    """Database aur table banane ke liye function"""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_text TEXT NOT NULL,
                due_date TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)
        conn.commit()

def add_task(task_text, due_date):
    """Naya task database mein insert karne ke liye"""
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (task_text, due_date, created_at) VALUES (?, ?, ?)",
            (task_text, due_date, created_at)
        )
        conn.commit()

def get_all_tasks():
    """Saare saved tasks ko fetch karne ke liye"""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, task_text, due_date FROM tasks ORDER BY due_date ASC")
        return cursor.fetchall()

def delete_task(task_id):
    """Task delete karne ke liye"""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()