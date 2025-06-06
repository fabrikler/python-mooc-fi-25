def line(number, symbol):
    if symbol == "":
        symbol = "*"
    result = number * symbol[0]
    print(result)

if __name__ == "__main__":
    line(5, "%")
    line(10, "LOL")
    line(5, "")