word = input("Please type in a word: ")
character = input("Please type in a character: ")

index = word.find(character)
slice = word[index:index+3]

if len(word) >= 3 and len(slice) >= 3:
    print(slice)
else:
    print()

