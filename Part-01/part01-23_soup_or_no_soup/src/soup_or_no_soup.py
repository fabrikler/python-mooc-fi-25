name = input("Please tell me your name:")

if name != "Jerry":
    portions = int(input("How many portions of soup?"))
    cost = portions * 5.90
    print("The total cost is", cost)
    print("Next please!")

if name == "Jerry":
    print("Next please!")