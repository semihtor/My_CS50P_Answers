import math

def main():
    fraction = input("Fraction: ")
    converted_fraction = convert(fraction)
    fuel_output = gauge(converted_fraction)
    print(fuel_output)


def convert(fraction):
    while True:
        try:
            dividend, divider = fraction.split("/") # dividend=bolunen divider=bolen
            new_dividend = int(dividend)
            new_divider = int(divider)
            fuel = new_dividend / new_divider
            if fuel <= 1: # dividend and divider are both int but dividend is greater than divider
                return int(round(fuel * 100))
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage > 98:
        return "F"
    else:
        return f"{math.ceil(percentage)}%"


if __name__ == "__main__":
    main()
