def no_vowels(word):

    new_string = ""

    vowel = "aeiou"

    for i in word:
        if i not in vowel:
            new_string += i
    return new_string


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))

