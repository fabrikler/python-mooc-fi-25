archive = []

while True:
    word = input("Word: ").lower()

    if word in archive:
        print(f"You typed in {(len(archive))} different words")
        break
    
    archive.append(word)
