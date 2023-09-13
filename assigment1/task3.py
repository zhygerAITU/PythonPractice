def modify_number(A):

    integer_part = int(A)
    fractional_part = A - integer_part

    modified_fractional_part = fractional_part * 100

    modified_integer_part = integer_part / 100

    new_number = modified_integer_part + modified_fractional_part / 100

    return round(new_number, 4)  

A = 12.34
new_number = modify_number(A)
print(f"The new number is: {new_number}")
