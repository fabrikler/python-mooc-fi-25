
word = input("Please type in a string: ")
length = len(word)
counter = 0

while length >= counter:
    print(f"{word[:counter]}")
    counter += 1