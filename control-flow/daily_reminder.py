# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task for today: ")
priority = input("Enter the priority level (high, medium, low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        reminder = f"Your task '{task}' is HIGH priority."
    case "medium":
        reminder = f"Your task '{task}' is MEDIUM priority."
    case "low":
        reminder = f"Your task '{task}' is LOW priority."
    case _:
        reminder = f"Your task '{task}' has an UNKNOWN priority."

# Check if task is time-sensitive
if time_bound == "yes":
    reminder += " This is time-sensitive and requires immediate attention today!"

# Provide a Customized Reminder
print("\n--- Daily Reminder ---")
print(reminder)
