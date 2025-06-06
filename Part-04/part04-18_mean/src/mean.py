def mean(my_list):
    my_mean = (sum(my_list) / len(my_list))
    return my_mean


if __name__ == "__main__":
    my_list = [2, 2, 2]
    result = mean(my_list)
    print(result)