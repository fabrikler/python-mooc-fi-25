
def hash_square(length):
    phrase = "#" * length

    while length > 0:
        print(phrase)
        length -= 1


if __name__ == "__main__":
    hash_square(5)