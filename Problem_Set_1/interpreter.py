userInput = input("File name: ").lower().strip()

x, y, z = userInput.split(" ")

match y:
    case "+":
        print("{:.1f}".format(float(x) + float(z)))
    case "-":
        print("{:.1f}".format(float(x) - float(z)))
    case "*":
        print("{:.1f}".format(float(x) * float(z)))
    case "/":
        print("{:.1f}".format(float(x) / float(z)))
