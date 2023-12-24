import sys
import csv

def check_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        return True
    else:
        sys.exit("Not a CSV file")

def main():
    check_arguments()
    temp = []

    try:
        with open(sys.argv[1], "r") as input_file:
            reader = csv.DictReader(input_file)
            for row in reader:
                last_name, first_name = row["name"].split(", ")
                temp.append({'first': first_name.lstrip(), 'last': last_name, 'house': row["house"]})
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]} does not exist")

    with open(sys.argv[2], "w") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in temp:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})



if __name__ == "__main__":
    main()
