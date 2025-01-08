import unittest
from tracker import Habit
from database import HabitDatabase
from datetime import datetime, timedelta

class TestHabitTracker(unittest.TestCase):

    def setUp(self):
        """
        This method will run before each test to set up any state.
        """
        #database initializing
        self.db = HabitDatabase("test_habits.db")

    def tearDown(self):
        """
        This method will run after each test to clean up the state.
        """
        #database delete after test
        pass

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

        #mark habit as completed
        habit.check_off()

        #streak increase to 1
        self.assertEqual(habit.get_streak(), initial_streak + 1)

    def test_add_habit_to_db(self):
        """
        Test if adding a habit to the database works.
        """
        self.db.add_habit("Exercise", "daily")
        habits = self.db.get_habits()
        self.assertGreater(len(habits), 0)
        self.assertEqual(habits[0][1], "Exercise") #this checks if the habit name is correctly stored

    def test_add_completion_to_db(self):
        """
        Test if habit completion is added to the database.
        """
        # Add a habit to the DB
        self.db.add_habit("Exercise", "daily")
        habit_id = self.db.get_habits()[0][0]

        #Add completion to the habit
        self.db.add_completion(habit_id)

        #Fetch completions and verify
        completions = self.db.connection.execute("SELECT * FROM completions").fetchall()
        self.assertGreater(len(completions), 0)
        self.assertEqual(completions[0][1], habit_id) # verify the completion is linked to the correct habit

    def test_streak_calculation(self):
        """
        Test streak calculation for a daily habit.
        """
        habit = Habit(name="Exercise", periodicity="daily")

        # Simulate completing the habit for a few days
        habit.check_off() # Day 1
        habit.completed_dates.append(datetime.now() - timedelta(days=1)) # Day 2

        # The streak should be 2
        self.assertEqual(habit.get_streak(), 2)

    def test_longest_streak(self):
        """
        Test calculating the longest streak for habits.
        """
        habit1 = Habit(name="Exercise", periodicity="daily")
        habit2 = Habit(name="Read", periodicity="daily")

        # Complete habits
        habit1.check_off()
        habit2.check_off()
        habit2.check_off()

        # Check longest streak between habit1 and habit2
        self.assertEqual(max(habit1.get_streak(), habit2.get_streak()), 2)

if __name__ == "__main__":
    unittest.main()