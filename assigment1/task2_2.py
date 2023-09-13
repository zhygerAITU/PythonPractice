def calculate():

    first_number = float(input("Enter the first number: "))

    operation = input("Enter the operation (+, -, *, /): ")

    second_number = float(input("Enter the second number: "))

    result = None  

    if operation == '+':
        result = first_number + second_number
    elif operation == '-':
        result = first_number - second_number
    elif operation == '*':
        result = first_number * second_number
    elif operation == '/':
        result = first_number / second_number if second_number != 0 else None
    else:
        print("Error: Invalid operation.")
        return

    if result is not None:
        print(f"{first_number} {operation} {second_number} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

calculate()
