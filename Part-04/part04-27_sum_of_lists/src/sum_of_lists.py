def list_sum(a: list, b: list):
    final = []

    for i in range(len(a)):
        final.append(a[i] + b[i])

    return final


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]