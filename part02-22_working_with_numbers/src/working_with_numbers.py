
counter = int()

addition = int()

negatives = int()

positives = int()

print("Please type in integer numbers. Type in 0 to finish.")

while True:
    number = int(input("Number:"))
    counter += 1
    addition += number
    
    if number < 0:
        negatives += 1

    if number > 0:
        positives += 1
    
    if number == 0:
        print("... the program asks for numbers")
        print(f"Numbers typed in {counter - 1}")
        print(f"The sum of the numbers is {addition}")
        print(f"The mean of the numbers is {addition / (counter - 1)}")
        print(f"Positive numbers {positives}")
        print(f"Negative numbers {negatives}")
        break

