def get_all_habits(habits):
    return [habit["name"] for habit in habits]

def get_habits_by_periodicity(habits, periodicity):
    return [habit for habit in habits if habit["periodicity"] == periodicity]

def get_longest_streak(habits):
    return max((habit.get_streak() for habit in habits), default=0)

def get_longest_streak_for_habit(habit):
    return habit.get_streak()