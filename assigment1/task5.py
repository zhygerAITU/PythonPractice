def guess_number():
    print("a) Multiply the planned number by 5.")
    print("b) Add 8.")
    print("c) Multiply the sum by 2.")
    
    result = int(input("Enter the final result: "))

    original_number = (result / 2) - 4

    print(f"The intended number is: {original_number}")

guess_number()
