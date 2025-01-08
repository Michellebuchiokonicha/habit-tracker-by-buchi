import sqlite3
from datetime import datetime

class HabitDatabase:
    def __init__(self, db_name="habits.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()
    
    def create_tables(self):
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS habits (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    periodicity TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
            """)
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS completions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    habit_id INTEGER,
                    completion_date TEXT NOT NULL,
                    FOREIGN KEY(habit_id) REFERENCES habits(id)
                )
             """)
            
    def add_habit(self, name, periodicity):
        with self.connection:
            self.connection.execute(
                "INSERT INTO habits (name, periodicity, created_at) VALUES (?, ?, ?)",
                (name, periodicity, datetime.now().isoformat())
            )

    def get_habits(self):
        with self.connection:
            return self.connection.execute("SELECT * FROM habits").fetchall()
    
    def add_completion(self,habit_id):
        with self.connection:
            self.connection.execute(
                "INSERT INTO completions (habit_id, completion_date) VALUES (?, ?)",
                (habit_id, datetime.now().isoformat())
            )