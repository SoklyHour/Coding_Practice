def main():
    while True:
        print("Menu:")
        print("1. Add numbers")
        print("2. Subtract numbers")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 + num2
            print(f"Sum: {result}")

        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 - num2
            print(f"Difference: {result}")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
