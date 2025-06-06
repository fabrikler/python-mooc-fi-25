students = int(input("How many students on the course?"))
desired_size = int(input("Desired group size?"))

if students % desired_size == 0:
    print(f"Number of groups formed: {students / desired_size}")

if students % desired_size != 0:
    print(f"Number of groups formed: {students // desired_size + 1}")

    

