import click
from datetime import datetime
from habit_tracker.tracker import Habit
from habit_tracker.database import HabitDatabase

@click.group()
def cli():
    pass

@cli.command()
@click.option("--name", prompt="Habit name", help="The name of the habit")
@click.option("--periodicity", prompt="Periodicity (daily/weekly)", help="The periodicity of the habit")
def add_habit(name, periodicity):
    """
    Add a new habit.
    """
    db = HabitDatabase()
    db.add_habit(name, periodicity)
    click.echo(f"Habit '{name}' with periodicity '{periodicity}' added!")

@cli.command()
def view_habits():
    """
    View all habits.
    """
    db = HabitDatabase()
    habits = db.get_habits()
    for habit in habits:
        click.echo(f"ID: {habit[0]}, Name: {habit[1]}, Periodicity: {habit[2]}")

@cli.command()
@click.option("--habit-id", prompt="Habit ID", help="The ID of the habit to mark as completed", type=int)
def mark_completion(habit_id):
    """
    Mark a habit as completed.
    """
    db = HabitDatabase()
    db.add_completion(habit_id)
    click.echo(f"Marked habit with ID {habit_id} as completed!")

@cli.command()
@click.option("--habit-id", prompt="Habit ID", help="The ID of the habit to delete", type=int)
def delete_habit(habit_id):
    """
    Delete a habit.
    """
    db = HabitDatabase()
    with db.connection:
        db.connection.execute("DELETE FROM habits WHERE id = ?", (habit_id,))
        db.connection.execute("DELETE FROM completions WHERE habit_id = ?", (habit_id,))
    click.echo(f"Deleted habit with ID {habit_id} and its completions.")

@cli.command()
@click.option("--habit-id", prompt="Habit ID", help="The ID of the habit to view the streak for", type=int)
def view_streak(habit_id):
    """
    View the current streak for a habit.
    """
    db = HabitDatabase()
    habits = db.get_habits()
    habit = next((h for h in habits if h[0] == habit_id), None)
    
    if not habit:
        click.echo(f"No habit found with ID {habit_id}")
        return
    
    # Calculate streak
    completions = db.connection.execute(
        "SELECT completion_date FROM completions WHERE habit_id = ?",
        (habit_id,)
    ).fetchall()
    completion_dates = [datetime.fromisoformat(row[0]) for row in completions]
    habit_obj = Habit(name=habit[1], periodicity=habit[2])
    habit_obj.completed_dates = completion_dates
    streak = habit_obj.get_streak()
    click.echo(f"The current streak for habit '{habit[1]}' is {streak}.")

if __name__ == "__main__":
    cli()
