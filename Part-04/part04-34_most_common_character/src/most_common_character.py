def most_common_character(char: str):
    
    highest_char = ""
    highest_count = 0

    for i in char:
        count = char.count(i)
        if count > highest_count:
            highest_char = i
            highest_count = count

    return highest_char


if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))
    
    first_string = "abc"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))