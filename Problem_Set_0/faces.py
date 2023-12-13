def convert(text):
    emojifiedMessage = text.replace(":)", "🙂").replace(":(", "🙁")

    return emojifiedMessage


def main():
    text = input("Enter the regular message: ")

    result = convert(text)

    print(result)


main()
