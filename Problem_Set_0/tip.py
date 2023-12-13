def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    formattedDollars = d.removeprefix("$")

    return float(formattedDollars)


def percent_to_float(p):
    formattedPercent = p.removesuffix("%")

    return float(formattedPercent) / 100


main()
