# Compatibility between Python 2 and Python 3
try:
    input = raw_input
except NameError:
    pass

# Habit Tracker v1.0
def main():
    while True:
        print("\nHabit Tracker - Version 1.0")
        print("1. Add a habit")
        print("2. View all habits")
        print("3. Exit")
        choice = input("Choose an option: ")
        break  # Temporary exit to test menu display & functionality

if __name__ == "__main__":
    main()