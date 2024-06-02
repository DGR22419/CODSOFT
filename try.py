def calculator():
    # Prompt the user to enter the first number
    num1 = float(input("Enter the first number: "))

    # Prompt the user to enter the second number
    num2 = float(input("Enter the second number: "))

    # Prompt the user to choose an operation
    print("Choose the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation = input("Enter the number corresponding to the operation: ")

    # Perform the calculation based on the chosen operation
    if operation == '1':
        result = num1 + num2
        operation_sign = "+"
    elif operation == '2':
        result = num1 - num2
        operation_sign = "-"
    elif operation == '3':
        result = num1 * num2
        operation_sign = "*"
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            operation_sign = "/"
        else:
            result = "undefined (division by zero is not allowed)"
            operation_sign = "/"
    else:
        result = "Invalid operation"
        operation_sign = ""

    # Display the result
    if operation_sign:
        print(f"The result of {num1} {operation_sign} {num2} is: {result}")
    else:
        print(result)

# Run the calculator
calculator()
