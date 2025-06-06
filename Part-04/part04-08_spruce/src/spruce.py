def spruce(reps):
    print("a spruce!")

    i = 0

    while i < reps:
        space = reps - i - 1
        stars = 2 * i + 1
        print(" " * space + "*" * stars)
        i += 1

    print(" " * (reps - 1) + "*")

if __name__ == "__main__":
    spruce(5)

 