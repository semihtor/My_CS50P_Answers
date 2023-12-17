def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum() and s[0].isalpha() and s[1].isalpha():
        for character in s:
            if character.isdigit():
                place = s.index(character)
                if character != "0" and s[place:].isdigit():
                    return True
                else:
                    return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
