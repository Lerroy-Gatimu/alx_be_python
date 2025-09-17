# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")

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
print(f"Reminder: {reminder}")
