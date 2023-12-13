def main():
    enteredTime = input("What time is it? ")
    convertedTime = convert(enteredTime)
    if 7 <= convertedTime <= 8:
        print("breakfast time")
    elif 12 <= convertedTime <= 13:
        print("lunch time")
    elif 18 <= convertedTime <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + (float(minutes) / 60)


if __name__ == "__main__":
    main()
