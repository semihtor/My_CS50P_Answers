month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    input_date = input("Date: ").strip()
    if "," in input_date:
        input_date = input_date.replace(",", "")
        input_month, input_day, input_year = input_date.split(" ")
        if input_month in month_names:
            input_month = month_names.index(input_month) + 1
    elif "/" in input_date:
        input_month, input_day, input_year = input_date.split("/")
    try:
        if int(input_month) > 12 or int(input_day) > 31:
            continue
        else:
            break
    except (ValueError, NameError):
        continue

print(input_year + "-" + f"{int(input_month):02}" + "-" + f"{int(input_day):02}")
