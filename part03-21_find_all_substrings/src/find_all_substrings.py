word = input("Please type in a word: ")
character = input("Please type in a character: ")

pos = 0

while True:
    index = word.find(character)
    if index == -1:
        break
    if index + 3 <= len(word):
        print(word[index:index+3])
        pos = index + 3
        word = word[index+1:]

    else:
        break