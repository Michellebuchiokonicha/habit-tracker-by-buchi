from datetime import datetime

class Habit:
    def __init__(self, name, periodicity):
        """
        Initialize a habit with a name and periodicity (daily or weekly).
        """
        self.name = name
        self.periodicity = periodicity
        self.created_at = datetime.now()
        self.completed_dates = [] #List of datetime objects when the task was completed

    def check_off(self):
        """
        Mark the habit as completed for the current date/time.
        """
        self.completed_dates.append(datetime.now())
    
    def get_streak(self):
        """
        the current streak based on periodicity.
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
                streak +1
            else:
                break
            current_date = date

        return streak