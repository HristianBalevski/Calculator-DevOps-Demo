# Demo calculator

def calculator():
    print("Welcome to the Calculator!")
    print("Select an operation to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        try:
            # Get the user's choice
            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice == "5":
                print("Exiting the calculator. Goodbye!")
                break

            if choice in ["1", "2", "3", "4"]:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == "1":
                    result = num1 + num2
                    print(f"The result is: {result}")
                elif choice == "2":
                    result = num1 - num2
                    print(f"The result is: {result}")
                elif choice == "3":
                    result = num1 * num2
                    print(f"The result is: {result}")
                elif choice == "4":
                    if num2 != 0:
                        result = num1 / num2
                        print(f"The result is: {result}")
                    else:
                        print("Error: Division by zero is not allowed.")
            else:
                print("Invalid choice. Please select a valid operation.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")


calculator()
