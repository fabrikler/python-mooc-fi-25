def line(number, symbol):
    if symbol == "":
        symbol = "*"
    result = number * symbol[0]
    print(result)

def square(size, character):
    i = 0
    while i < size:
        line(size, character)
        i += 1

if __name__ == "__main__":
    square(6, "x")