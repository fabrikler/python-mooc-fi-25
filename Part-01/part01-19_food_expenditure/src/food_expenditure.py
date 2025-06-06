frequency = int(input("How many times a week do you eat at the student cafeteria?")) 
price = float(input("The price of a typical student lunch?"))
groceries = float(input("How much money do you spend on groceries in a week?\n"))

total_week = groceries + frequency * price

print("\nAverage food expediture:")
print(f"Daily: {total_week / 7} euros")
print(f"Weekly: {total_week} euros")

