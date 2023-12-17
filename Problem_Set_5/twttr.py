def main():
    input_message = input("Input: ").strip()
    print(shorten(input_message))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    output_message = ""

    for i in range(len(word)):
        if word[i] not in vowels:
            output_message += word[i]

    return output_message


if __name__ == "__main__":
    main()
