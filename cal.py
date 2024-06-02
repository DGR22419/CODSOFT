def calculator():
    try : 
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

    except :
        calculator()
        
    print("Choose the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation = input("Enter the number corresponding to the operation: ")

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

    if operation_sign:
        print(f"The result of {num1} {operation_sign} {num2} is: {result}")
    else:
        print(result)

calculator()
