from math import sqrt

while True:
    number = int(input("Please type in a number:"))

    if number < 0:
        print("Invalid number")

    elif number == 0:
        break
       
    elif number > 0:
        root = (sqrt(number))
        print(float(root))
        
print("Exiting...")

 
  

