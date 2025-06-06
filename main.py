# main.py

from food_ordering_app import FoodOrderingApp  

def main():
    app = FoodOrderingApp()

    while True:
        print("\nWelcome to Food Ordering System")
        print("1. Start Order")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            app.start_order()
        elif choice == '2':
            print("Thank you for visiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
