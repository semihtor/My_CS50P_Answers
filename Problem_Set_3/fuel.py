import math

while True:
    fraction = input("Fraction: ")

    try:
        dividend, divider = fraction.split("/") # dividend=bolunen divider=bolen

        new_dividend = int(dividend)

        new_divider = int(divider)

        fuel = new_dividend / new_divider

        if fuel <= 1: # dividend and divider are both int but dividend is greater than divider

            break

    except (ValueError, ZeroDivisionError):

        continue

percentage = int(round(fuel * 100))

if percentage <= 1:
    print("E")
elif percentage > 98:
    print("F")
else:
    print(f"{math.ceil(percentage)}%")
