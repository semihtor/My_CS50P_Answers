import sys

def check_arguments():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].endswith(".py"):
        return True
    else:
        sys.exit("Not a Python file")

def check_for_only_code(line):
    if line.isspace():
        return False
    if line.lstrip().startswith("#"):
        return False
    return True

def main():
    check_arguments()

    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    line_count = 0
    for line in lines:
        if check_for_only_code(line) == True:
            line_count += 1
    print(line_count)

if __name__ == "__main__":
    main()
