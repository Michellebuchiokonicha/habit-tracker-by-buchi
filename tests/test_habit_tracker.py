import unittest
from habit_tracker.tracker import Habit
from habit_tracker.database import HabitDatabase
from datetime import datetime, timedelta
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../habit_tracker')))

from habit_tracker.tracker import Habit
from habit_tracker.database import HabitDatabase



class TestHabitTracker(unittest.TestCase):

    def setUp(self):
        """
        This method will run before each test to set up any state.
        """
        # Database initializing for tests
        self.db = HabitDatabase("test_habits.db")

    def tearDown(self):
        """
        This method will run after each test to clean up the state.
        """
        if os.path.exists("test_habits.db"):
            os.remove("test_habits.db")

    def test_create_habit(self):
        """
        Test habit creation.
        """
        habit = Habit(name="Exercise", periodicity="daily")
        self.assertEqual(habit.name, "Exercise")
        self.assertEqual(habit.periodicity, "daily")
        self.assertIsInstance(habit.created_at, datetime)

    def test_habit_checkoff(self):
        """
        Test marking a habit as completed.
        """
        habit = Habit(name="Exercise", periodicity="daily")
        initial_streak = habit.get_streak()

        # Mark habit as completed
        habit.check_off()

        # Streak increases to 1
        self.assertEqual(habit.get_streak(), initial_streak + 1)

    def test_add_habit_to_db(self):
        """
        Test if adding a habit to the database works.
        """
        self.db.add_habit("Exercise", "daily")
        habits = self.db.get_habits()
        self.assertGreater(len(habits), 0)
        self.assertEqual(habits[0][1], "Exercise") 

    def test_add_completion_to_db(self):
        """
        Test if habit completion is added to the database.
        """
        # Add a habit to the DB
        self.db.add_habit("Exercise", "daily")
        habit_id = self.db.get_habits()[0][0]

        # Add completion to the habit
        self.db.add_completion(habit_id)

        # Fetch completions and verify
        completions = self.db.connection.execute("SELECT * FROM completions").fetchall()
        self.assertGreater(len(completions), 0)
        self.assertEqual(completions[0][1], habit_id)  

    def test_streak_calculation(self):
        """
        Test streak calculation for a daily habit.
        """
        # Add a habit to the DB and fetch it
        self.db.add_habit("Exercise", "daily")
        habit_id = self.db.get_habits()[0][0]
        habit = Habit(name="Exercise", periodicity="daily")
        habit.completed_dates.append(datetime.now() - timedelta(days=1)) 
        # Add completion to the database
        self.db.add_completion(habit_id)

        # Simulate completing the habit today
        habit.check_off()

        # The streak should be 2 (past completion + today)
        self.assertEqual(habit.get_streak(), 2)

    def test_longest_streak(self):
        """
        Test calculating the longest streak for habits.
        """
        # Add two habits to the DB
        self.db.add_habit("Exercise", "daily")
        self.db.add_habit("Read", "daily")
        
        # Fetch the habits from the database
        habits_data = self.db.get_habits()
        habit1 = Habit(name=habits_data[0][1], periodicity=habits_data[0][2])
        habit2 = Habit(name=habits_data[1][1], periodicity=habits_data[1][2])

        # Complete habits
        habit1.check_off()
        habit2.check_off()
        habit2.check_off() 

        # Check the longest streak between habit1 and habit2
        self.assertEqual(max(habit1.get_streak(), habit2.get_streak()), 2)

if __name__ == "__main__":
    unittest.main()