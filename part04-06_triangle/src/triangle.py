def line(number, symbol):
    if symbol == "":
        symbol = "*"
    result = number * symbol[0]
    print(result)

def triangle(size):
    i = 1
    while i <= size:
        line(i, "#")
        i += 1

if __name__ == "__main__":
    triangle(10)

