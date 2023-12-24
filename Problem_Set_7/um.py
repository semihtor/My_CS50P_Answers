import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um_counted = re.findall(r"\b(um)\b", s, re.IGNORECASE)
    return len(um_counted)



if __name__ == "__main__":
    main()
