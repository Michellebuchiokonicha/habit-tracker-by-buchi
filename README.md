# habit-tracker-by-buchi..
This is a simple habit tracker backend implementation using Python object-oriented and functional programming.

## Habit Tracker

This is a Python-based habit tracker application that allows users to create, manage, and track their habits over time. The app supports tracking daily and weekly habits, marking them as completed, and analyzing streaks and task completion patterns.

## Features
- Create daily and weekly habits.
- Mark habits as completed.
- Track streaks for each habit.
- Perform analytics on your habits, such as finding the longest streak or viewing missed tasks.
- Store habit data using an SQLite database.
- Command-line interface (CLI) for easy interaction.
- Ability to delete habits and view streaks.

## Project Structure
- `main.py`: Entry point of the application, handles CLI commands for interacting with habits.
- `database.py`: Handles all database operations related to habits and completions.
- `tracker.py`: Manages habit tracking logic, including habit creation, completion, and streak calculation.
- `analytics.py`: Provides analytical tools for habits, such as finding the longest streak.
- `test.py`: Contains unit tests for the habit tracker functionality.

## How to Run
1. Clone the repository:
    ```bash
    git clone https://github.com/michellebuchiokonicha/habit-tracker.git
    cd habit-tracker
    ```

2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python main.py
    ```

## CLI Commands
- **add_habit**: Add a new habit.
    ```bash
    python main.py add-habit --name "Exercise" --periodicity "daily"
    ```

- **view_habits**: View all habits.
    ```bash
    python main.py view-habits
    ```

- **mark_completion**: Mark a habit as completed.
    ```bash
    python main.py mark-completion --habit-id 1
    ```

- **delete_habit**: Delete a habit.
    ```bash
    python main.py delete-habit --habit-id 1
    ```

- **view_streak**: View the current streak for a habit.
    ```bash
    python main.py view-streak --habit-id 1
    ```

## Requirements
- Python 3.11
- Libraries:
    - `click` for CLI
    - `sqlite3` for database operations
    - `datetime` for date/time handling

## Tests
To run the unit tests for this project:
```bash
python -m unittest test.py
