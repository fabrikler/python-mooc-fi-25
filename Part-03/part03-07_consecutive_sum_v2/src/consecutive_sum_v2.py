limit = int(input("Limit: "))
counter = 1
summe = 0
phrase =""

while summe < limit:
    summe += counter
    phrase += f"{counter} + "
    counter += 1

print(f"The consecutive sum: {phrase[:-3]} = {summe}")

