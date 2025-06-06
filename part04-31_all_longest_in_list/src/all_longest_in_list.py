def all_the_longest(my_list: list):

    max_len = 0

    for i in my_list:
        if len(i) > max_len:
            max_len = len(i)

    long_list = []

    for i in my_list:
        if len(i) == max_len:
            long_list.append(i)

    return long_list


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']
