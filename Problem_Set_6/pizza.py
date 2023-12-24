import sys
import csv
from tabulate import tabulate

def check_arguments():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].endswith(".csv"):
        return True
    else:
        sys.exit("Not a CSV file")

def main():
    check_arguments()

    menu = []

    try:
        with open(sys.argv[1], "r") as csvmenu:
            reader = csv.reader(csvmenu)
            for row in reader:
                menu.append(row)
        print(tabulate(menu, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
