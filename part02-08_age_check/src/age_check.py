# Write your solution here

age = int(input("What is your age?"))

if age >= 0 and age <= 4:
    print("I suspect you can't write quite yet.")

elif age > 4 and age < 100: 
    print(f"Ok, you're {age} years old")

elif age > 100 and age <= 120: 
    print("You are older than the oldest tree in my garden.")

else: 
    print("That must be a mistake")