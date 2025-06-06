gift = float(input("Value of gift: "))


if gift < 5000:
    print("No tax!")

elif gift > 5000 and gift < 25000:
    tax = float(100 + (gift-5000) * float(0.08))

elif gift > 25000 and gift < 55000:
    tax = float(1700 + (gift-25000) * float(0.10))

elif gift > 55000 and gift < 200000:
    tax = float(4700 + (gift-55000) * float(0.12))

elif gift > 200000 and gift < 1000000:
    tax = float(22100 + (gift-200000) * float(0.15))

elif gift > 1000000:
   tax = float(142100 + (gift-1000000) * float(0.17))

if gift >= 5000:
    print(f"Amount of tax: {float(tax)} euros")
