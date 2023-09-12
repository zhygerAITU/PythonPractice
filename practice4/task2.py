def calculate_sum_and_count(sequence):
    total_sum = sum(sequence)
    num_count = len(sequence)
    return total_sum, num_count

sequence = [1, 2, 3, 4, 0]  
total_sum, num_count = calculate_sum_and_count(sequence)

print(f"The sum of all numbers in the sequence is: {total_sum}")
print(f"The number of all numbers in the sequence is: {num_count}")
