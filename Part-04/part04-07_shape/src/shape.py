def line(number, symbol):
    if symbol == "":
        symbol = "*"
    result = number * symbol[0]
    print(result)

def shape(size, symbol, height, rectangle):
    i = 1
    while i <= size:
        line(i, symbol)
        i += 1
    i = 1
    while i <= height:
        line(size, rectangle)
        i += 1
    
if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")

