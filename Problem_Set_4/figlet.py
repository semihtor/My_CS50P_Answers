import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

available_fonts = figlet.getFonts()

if len(sys.argv) == 1:
    # print("no font given")
    figlet.setFont(font=random.choice(available_fonts))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in available_fonts):
    # print("correct font arguments given")
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

user_input = input("Input: ")

print("Output: \n" + figlet.renderText(user_input))
