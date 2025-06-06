def longest_series_of_neighbours(sample: list):

    counter = 1
    length = 1

    for i in range(len(sample) -1):

        if sample[i] - sample[i+1] == 1 or sample[i] - sample[i+1] == -1:
            counter += 1

            if counter > length:
                length = counter

        else:
            counter = 1

    return length
            

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))