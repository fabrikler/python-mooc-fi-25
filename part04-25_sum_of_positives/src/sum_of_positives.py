def sum_of_positives(mylist):
    positives =[]

    for i in mylist:
        if i > 0:
            positives.append(i)
    return sum(positives)


if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)

