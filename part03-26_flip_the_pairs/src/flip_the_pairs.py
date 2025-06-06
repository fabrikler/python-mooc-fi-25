number = int(input("Please type in a number: "))

counter = 1

while counter + 1 <= number:
    print(counter + 1)
    print(counter)
    counter += 2

if counter <= number:
    print(counter)
