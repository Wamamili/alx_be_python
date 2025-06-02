# daily_reminder Reminds the user about a single priority task.

def main():
    while True:
        # Prompt for task details
        task = input("Enter your task: ").strip()
        priority = input("Priority (high/medium/low): ").strip().lower()
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

        print()  # Blank line for readability

        # Process the task using match-case (Python 3.10+)
        match priority:
            case "high":
                message = f"'{task}' is a high priority task"
            case "medium":
                message = f"'{task}' is a medium priority task"
            case "low":
                message = f"'{task}' is a low priority task"
            case _:
                print("Invalid priority entered. Please enter high, medium, or low.\n")
                continue  # Restart loop for valid input

        # Add time-sensitivity info
        if time_bound == "yes":
            message += " that requires immediate attention today!"
        elif time_bound == "no":
            message += ". Consider completing it when you have free time."
        else:
            print("Invalid time-bound input. Please enter yes or no.\n")
            continue  # Restart loop for valid input

        # Print the reminder
        print("Reminder:", message)
        break  # Exit loop after successful input and output

if __name__ == "__main__":
    main()
