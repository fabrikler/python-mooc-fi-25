password1 = input("Password:")

while True:

    password2 = input("Repeat password:")

    if password2 == password1:
        break
    print("They do not match!")

print("User account created!")



