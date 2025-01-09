from datetime import datetime

class Habit:
    """
    Represents a habit with tracking capabilities.

    Attributes:
        name (str): The name of the habit.
        periodicity (str): Frequency of the habit ('daily' or 'weekly').
        created_at (datetime): Timestamp when the habit was created.
        completed_dates (list): List of datetime objects when the habit was completed.
    """

    def __init__(self, name, periodicity):
        """
        Initialize a habit with a name and periodicity.

        Args:
            name (str): The name of the habit.
            periodicity (str): The frequency of the habit ('daily' or 'weekly').
        """
        self.name = name
        self.periodicity = periodicity
        self.created_at = datetime.now()
        self.completed_dates = []  # List of datetime objects when the task was completed

    def check_off(self):
        """
        Mark the habit as completed for the current date/time.
        """
        self.completed_dates.append(datetime.now())

    def get_streak(self):
        """
        Calculate the current streak of habit completions based on periodicity.

        Returns:
            int: The current streak count.
        """
        if not self.completed_dates:
            return 0

        streak = 0
        sorted_dates = sorted(self.completed_dates)
        current_date = sorted_dates[0]

        for date in sorted_dates:
            if self.periodicity == "daily" and (date - current_date).days <= 1:
                streak += 1
            elif self.periodicity == "weekly" and (date - current_date).days <= 7:
                streak += 1
            else:
                break
            current_date = date

        return streak
