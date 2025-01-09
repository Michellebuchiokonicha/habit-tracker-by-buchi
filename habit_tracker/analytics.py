from datetime import datetime
from habit_tracker.tracker import Habit
from habit_tracker.database import HabitDatabase

"""
Provides analytical and visualization tools for habits.

Functions:
    get_all_habits: Returns the names of all habits.
    get_habits_by_periodicity: Filters habits by periodicity.
    get_longest_streak: Finds the longest streak across all habits.
    get_longest_streak_for_habit: Finds the longest streak for a single habit.
"""

def get_all_habits(habits):
    """
    Get the names of all habits.
    
    Args:
        habits (list): List of habit objects (from the HabitDatabase).
    
    Returns:
        list: List of habit names.
    """
    return [habit.name for habit in habits]

def get_habits_by_periodicity(habits, periodicity):
    """
    Filter habits by their periodicity (daily or weekly).
    
    Args:
        habits (list): List of habit objects.
        periodicity (str): The periodicity to filter by ('daily' or 'weekly').
    
    Returns:
        list: List of habits with the specified periodicity.
    """
    return [habit for habit in habits if habit.periodicity == periodicity]

def get_longest_streak(habits):
    """
    Get the longest streak across all habits.
    
    Args:
        habits (list): List of habit objects.
    
    Returns:
        int: The longest streak.
    """
    return max((habit.get_streak() for habit in habits), default=0)

def get_longest_streak_for_habit(habit):
    """
    Get the longest streak for a single habit.
    
    Args:
        habit (Habit): The habit object.
    
    Returns:
        int: The longest streak for the specified habit.
    """
    return habit.get_streak()

def get_habits_from_db():
    """
    Retrieve all habits from the database and return them as Habit objects.
    
    Returns:
        list: List of Habit objects.
    """
    db = HabitDatabase()
    habits_data = db.get_habits()
    habits = []

    for habit_data in habits_data:
        habit = Habit(name=habit_data[1], periodicity=habit_data[2])
        # Fetch and set completed dates for the habit
        completions = db.get_completions(habit_data[0])
        habit.completed_dates = [datetime.fromisoformat(row[0]) for row in completions]
        habits.append(habit)

    return habits
