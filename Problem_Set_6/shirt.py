import sys
import os
from PIL import Image, ImageOps

def check_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif os.path.splitext(sys.argv[1].lower())[1] != os.path.splitext(sys.argv[2].lower())[1]:
        sys.exit("Input and output have different extensions")
    elif (os.path.splitext(sys.argv[1].lower())[1] not in [".jpg", ".jpeg", ".png"]):
        sys.exit("Invalid input")
    elif (os.path.splitext(sys.argv[2].lower())[1] not in [".jpg", ".jpeg", ".png"]):
        sys.exit("Invalid output")
    else:
        return True

def main():
    check_arguments()

    try:
        muppet = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Input does not exist")

    resized_muppet = ImageOps.fit(muppet, size=shirt.size)

    resized_muppet.paste(shirt, shirt)

    resized_muppet.save(sys.argv[2])

if __name__ == "__main__":
    main()
