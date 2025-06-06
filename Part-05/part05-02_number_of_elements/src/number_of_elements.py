def count_matching_elements(my_matrix: list, element: int):

    megamatch = 0

    for row in my_matrix:
        for i in row:
            if i == element:
                megamatch += 1

    return megamatch



if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))





