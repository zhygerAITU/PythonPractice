def calculate_cost(price_per_kg):
    for kg in range(1, 11):
        total_cost = kg * price_per_kg
        print(f"{kg} kg of sweets costs: ${total_cost:.2f}")

price_per_kg = float(input("Enter the price of 1 kg of sweets: $"))

calculate_cost(price_per_kg)
