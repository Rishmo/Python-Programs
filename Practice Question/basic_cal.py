# num1= int(input("Enter First number: "))
# num2= int(input("Enter Second number: "))

# print("Sum: ", num1+num2)
# print("Difference: ", num1-num2)
# print("Multiply: ", num1*num2)
# print("Divide: ", num1/num2)

def calculator():
    print("Welcome to the Basic Calculator!")
    print("Select an operation to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get user input
    choice = input("Enter the number corresponding to the operation (1/2/3/4): ")

    # Ensure valid input
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice! Please select a valid operation.")
        return

    try:
        # Get numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the selected operation
        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
    except ValueError:
        print("Invalid input! Please enter numerical values.")

# Run the calculator
calculator()
