def print_many_times(text, times):
    counter = 0

    while times > counter:
        print(text)
        counter += 1

if __name__ == "__main__":
    print_many_times("python", 5)