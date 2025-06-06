def palindromes(word):
    mylist = list(word)
    newlist = []
    i = -1

    for n in mylist:
        newlist.append(mylist[i])
        i -= 1
    
    return mylist == newlist

while True:
    word = input("Please type in a palindrome: ")

    if palindromes(word):
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

if __name__ == "__main__":
     palindromes(word)