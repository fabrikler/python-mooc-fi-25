def line(number, symbol):
    if symbol == "":
        symbol = "*"
    result = number * symbol[0]
    print(result)


def box_of_hashes(height):
    while height > 0:
        line(10, "#")
        height -= 1


if __name__ == "__main__":
    box_of_hashes(5)
    print()
    box_of_hashes(2)

    