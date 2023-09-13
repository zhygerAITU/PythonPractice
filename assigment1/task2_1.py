def calculate():
    
    first_number = float(input("Enter the first number: "))

    operation = input("Enter the operation (+, -, *, /): ")

    second_number = float(input("Enter the second number: "))

    if operation == '+':
        result = first_number + second_number
    elif operation == '-':
        result = first_number - second_number
    elif operation == '*':
        result = first_number * second_number
    elif operation == '/':
        # Check for division by zero
        if second_number != 0:
            result = first_number / second_number
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Error: Invalid operation.")
        return

    print(f"{first_number} {operation} {second_number} = {result}")

calculate()
