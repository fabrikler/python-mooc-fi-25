def greatest_number(a, b, c):

    max = a

    if b > max:
        max = b
    if c > max:
        max = c

    return max


if __name__ == "__main__":
    print(greatest_number(3, 4, 1)) # 4
    print(greatest_number(99, -4, 7)) # 99
    print(greatest_number(0, 0, 0)) # 0