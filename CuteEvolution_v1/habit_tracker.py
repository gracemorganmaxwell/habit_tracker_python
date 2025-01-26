# Global set to store habits
habits = set()

def main():
    while True:
        print("\nHabit Tracker - Version 1.0")
        print("1. Add a habit")
        print("2. View all habits")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            habit = input("Enter a habit: ").strip()
            if habit:
                if habit in habits:
                    print("'%s' is already in your habits list!" % habit)
                else:
                    habits.add(habit)
                    print("'%s' has been added to your habits." % habit)
            else:
                print("Please enter a valid habit.")
        elif choice == "2":
            if habits:
                print("\nYour habits:")
                for habit in habits:
                    print("- %s" % habit)
            else:
                print("You haven't added any habits yet.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()