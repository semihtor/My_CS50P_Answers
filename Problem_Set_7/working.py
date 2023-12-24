import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if is_format_correct := re.search(r"^(([1-9]|1[0-2]*):*(0[0-9]|[1-5][0-9])*) (AM|PM) to (([1-9]|1[0-2]*):*(0[0-9]|[1-5][0-9])*) (AM|PM)$", s):
        start_clock, start_hour, start_minute, start_meridiem, finish_clock, finish_hour, finish_minute, finish_meridiem = is_format_correct.groups()

        if int(start_hour) > 12 or int(finish_hour) > 12:
            raise ValueError
        start_time = convert_to_24h(start_hour, start_minute, start_meridiem)
        finish_time = convert_to_24h(finish_hour, finish_minute, finish_meridiem)
        return start_time + " to " + finish_time
    else:
        raise ValueError

def convert_to_24h(hour, minute, meridiem):
    if meridiem == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)

    if minute == None:
        new_time = f"{new_hour:02}" + ":00"
    else:
        new_time = f"{new_hour:02}" + ":" + minute
    return new_time

if __name__ == "__main__":
    main()
