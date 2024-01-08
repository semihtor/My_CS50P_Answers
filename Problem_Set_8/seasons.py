from datetime import date
import inflect
import re
import sys


def main():

    p = inflect.engine()

    date_of_birth = input("Date of Birth: ")

    try:
        year, month, day = check_date_of_birth(date_of_birth)
    except:
        sys.exit("Invalid date")

    converted_date_of_birth = date(int(year), int(month), int(day))

    current_date = date.today()

    date_delta = current_date - converted_date_of_birth

    elapsed_minutes = date_delta.days * 24 * 60

    elapsed_minutes_in_words = p.number_to_words(elapsed_minutes, andword="").capitalize()

    print(elapsed_minutes_in_words + " minutes")




def check_date_of_birth(date_of_birth):

    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", date_of_birth):
        y, m, d = date_of_birth.split("-")
        return y, m, d


if __name__ == "__main__":
    main()
