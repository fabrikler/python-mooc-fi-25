pin = 4321
attempts = 0

while True:
    code = int(input("PIN:"))
    attempts += 1

    if code == pin and attempts == 1:
        print("Correct! It only took you one single attempt!")
        break

    if code != pin:
        print("Wrong")

    if code == pin and attempts > 1:
        print(f"Correct! It took you {attempts} attempts")
        break

