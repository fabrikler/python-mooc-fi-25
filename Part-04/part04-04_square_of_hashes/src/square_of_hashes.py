def line(number, symbol):
    if symbol == "":
        symbol = "*"
    result = number * symbol[0]
    print(result)

def square_of_hashes(size):
    height = size
    while size > 0:
        line(height, "#")
        size -= 1

if __name__ == "__main__":
    square_of_hashes(5)
    print()
    square_of_hashes(3)