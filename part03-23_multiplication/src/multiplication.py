number = int(input("Please type in a number: "))

op1 = 1

while op1 <= number:
    op2 = 1  
    while op2 <= number:
        print(f"{op1} x {op2} = {op1 * op2}")
        op2 += 1 
    op1 += 1