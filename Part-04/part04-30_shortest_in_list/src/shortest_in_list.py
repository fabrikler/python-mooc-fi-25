def shortest(my_list: list):

    shortest = my_list[0]

    for i in my_list:
        if len(i) < len(shortest):
            shortest = i
    return shortest


if __name__ == "__main__":
    my_list = ["gagaga", "gaga", "gagagaga", "gaa"]
    result = shortest(my_list)
    print(result)