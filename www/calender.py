import datetime

# Dictionary to store events
calendar = {}

def add_event(date, event):
    """Add an event to the calendar."""
    if date in calendar:
        calendar[date].append(event)
    else:
        calendar[date] = [event]
    print(f"Event '{event}' added on {date}.")

def view_events(date):
    """View events for a specific date."""
    if date in calendar:
        print(f"Events on {date}:")
        for i, event in enumerate(calendar[date], start=1):
            print(f"{i}. {event}")
    else:
        print(f"No events found on {date}.")

def delete_event(date, event_index):
    """Delete an event from the calendar."""
    if date in calendar and 0 < event_index <= len(calendar[date]):
        removed_event = calendar[date].pop(event_index - 1)
        print(f"Event '{removed_event}' removed from {date}.")
        if not calendar[date]:  # Remove the date if no events remain
            del calendar[date]
    else:
        print("Invalid date or event index.")

def main():
    """Main function to manage the calendar."""
    while True:
        print("\nCalendar Menu:")
        print("1. Add Event")
        print("2. View Events")
        print("3. Delete Event")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")  # Validate date format
                event = input("Enter the event description: ")
                add_event(date, event)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")  # Validate date format
                view_events(date)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")  # Validate date format
                view_events(date)
                if date in calendar:
                    event_index = int(input("Enter the event number to delete: "))
                    delete_event(date, event_index)
            except ValueError:
                print("Invalid input. Please use the correct format.")
        elif choice == "4":
            print("Exiting the calendar. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()