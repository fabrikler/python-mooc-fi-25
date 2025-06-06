# Write your solution here

print("Person 1:")

person1 = input("Name: ")
person1_age = int(input("Age: "))

print("Person 2:")

person2 = input("Name: ")
person2_age = int(input("Age: "))

if person1_age > person2_age:
    print(f"The elder is {person1}")

elif person2_age > person1_age:
    print(f"The elder is {person2}")

else:
    print(f"{person1} and {person2} are the same age")