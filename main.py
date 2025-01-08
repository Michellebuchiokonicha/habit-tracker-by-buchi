import click
from tracker import Habit
from database import HabitDatabase

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

if __name__== "__main__":
    cli()