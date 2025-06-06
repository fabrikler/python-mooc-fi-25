words = ""

scanner = ""

while True:
    word = input("Please type in a word: ")

    if word == "end":
        break

    if word == scanner:
        break
      
    words += word + (" ")
    scanner = word

print(words)
