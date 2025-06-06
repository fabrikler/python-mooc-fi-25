
while True:
    factor1 = 1
    factor2 = 1

    result = factor1 * factor2

    number = int(input("Please type in a number: "))

    if number <= 0:
        print("Thanks and bye!")
        break

    while number > 0 and number >= factor1:
        result *= factor1
        factor1 += 1
    print(f"The factorial of the number {number} is {result}")









    



