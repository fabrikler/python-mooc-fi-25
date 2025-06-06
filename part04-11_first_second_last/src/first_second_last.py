def first_word(sentence):
    i = 0
    word1 = ""
    
    while i < len(sentence):
        if sentence[i] == " ":
            break
        word1 += sentence[i]
        i += 1
        
    return word1

def second_word(sentence):

    i = 0

    while i < len(sentence) and sentence[i] != " ":
        i += 1

    while i < len(sentence) and sentence[i] == " ":
        i += 1

    word2 = ""

    while i < len(sentence) and sentence[i] != " ":
        word2 += sentence[i]
        i += 1

    return word2

def last_word(sentence):

    i = len(sentence) - 1
    last = ""

    while i < len(sentence) and sentence[i] != " ":
        i -= 1
    
    i += 1
    
    while i < len(sentence):
        last += sentence[i]
        i += 1

    return last


if __name__ == "__main__":
    sentence = "it was a dark and stormy python"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))







