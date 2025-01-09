import sqlite3
from datetime import datetime

class HabitDatabase:
    """
    Handles database operations for the habit tracker.

    Attributes:
        connection (sqlite3.Connection): Connection to the SQLite database.

    Methods:
        create_tables: Creates necessary tables if they don't exist.
        add_habit: Adds a new habit to the database.
        get_habits: Retrieves all habits from the database.
        add_completion: Records a completion for a habit.
        delete_habit: Deletes a habit and its completions.
        get_completions: Retrieves all completions for a specific habit.
    """

    def __init__(self, db_name="habits.db"):
        """
        Initialize the HabitDatabase and create tables if necessary.

        Args:
            db_name (str): Name of the SQLite database file.
        """
        self.connection = sqlite3.connect(db_name)
        self.create_tables()
    
    def create_tables(self):
        """
        Create tables for storing habits and completions.
        """
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
        """
        Add a new habit to the database.

        Args:
            name (str): Name of the habit.
            periodicity (str): Periodicity of the habit ('daily' or 'weekly').
        """
        with self.connection:
            self.connection.execute(
                "INSERT INTO habits (name, periodicity, created_at) VALUES (?, ?, ?)",
                (name, periodicity, datetime.now().isoformat())
            )

    def get_habits(self):
        """
        Retrieve all habits from the database.

        Returns:
            list: List of tuples containing habit details.
        """
        with self.connection:
            return self.connection.execute("SELECT * FROM habits").fetchall()
    
    def add_completion(self, habit_id):
        """
        Record a completion for a habit.

        Args:
            habit_id (int): ID of the habit to mark as completed.
        """
        with self.connection:
            self.connection.execute(
                "INSERT INTO completions (habit_id, completion_date) VALUES (?, ?)",
                (habit_id, datetime.now().isoformat())
            )
    
    def delete_habit(self, habit_id):
        """
        Delete a habit and its associated completions.

        Args:
            habit_id (int): ID of the habit to delete.
        """
        with self.connection:
            self.connection.execute("DELETE FROM habits WHERE id = ?", (habit_id,))
            self.connection.execute("DELETE FROM completions WHERE habit_id = ?", (habit_id,))
    
    def get_completions(self, habit_id):
        """
        Retrieve all completions for a specific habit.

        Args:
            habit_id (int): ID of the habit.

        Returns:
            list: List of completion dates as strings.
        """
        with self.connection:
            return self.connection.execute(
                "SELECT completion_date FROM completions WHERE habit_id = ?",
                (habit_id,)
            ).fetchall()
