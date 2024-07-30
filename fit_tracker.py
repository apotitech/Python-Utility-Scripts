import datetime
import random

def create_sample_steps_file(filename='steps.txt', days=365):
    """Creates a sample steps file with random step counts for each day of the year."""
    random.seed(0)  # Seed for reproducible results
    with open(filename, 'w') as file:
        for _ in range(days):
            file.write(f"{random.randint(0, 20000)}\n")

def fitness_tracker_analysis(filename):
    """
    Analyzes and displays data from a fitness tracker with error handling.

    Args:
        filename (str): Path to the file containing daily step counts for a year.

    Returns:
        None. Prints the average number of steps taken each month and the number
        of days with more than 10,000 steps.
    """

    # Initialize variables
    steps_per_month = {}
    days_over_10000 = 0
    start_date = datetime.date(2020, 1, 1)  # Assuming the year starts from January 1st

    try:
        # Read file and process data
        with open(filename, 'r') as file:
            for day, line in enumerate(file, start=1):
                try:
                    steps = int(line.strip())
                    date = start_date + datetime.timedelta(days=day-1)
                    month = date.strftime('%B')
                    steps_per_month.setdefault(month, []).append(steps)

                    if steps > 10000:
                        days_over_10000 += 1

                except ValueError:
                    print(f"Invalid data: '{line.strip()}'")
                except Exception as e:
                    print(f"Unexpected error processing line: '{line.strip()}'. Error: {e}")

        # Calculate and display monthly averages
        for month, steps in steps_per_month.items():
            average_steps = sum(steps) / len(steps)
            print(f"Average steps in {month}: {average_steps:.0f}")

        # Display number of days with more than 10,000 steps
        print(f"Days with more than 10,000 steps: {days_over_10000}")

    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Unexpected error reading file: {e}")

# Create sample Steps.txt file and run analysis
create_sample_steps_file()
fitness_tracker_analysis('steps.txt')
