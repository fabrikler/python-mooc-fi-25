list = []
i = 1

while True: 
    print(f"The list is now {list}")
    arrow = input("a(d)d, (r)emove or e(x)it: ").lower()

    if arrow == "x":
        print("Bye!")
        break
    if arrow == "d":
        list.append(i)
        i += 1
    if arrow == "r":
        list.pop()
        i -= 1
    
    

    

