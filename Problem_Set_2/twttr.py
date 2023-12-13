input_message = input("Input: ").strip()

output_message = ""

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for i in range(len(input_message)):
    if input_message[i] not in vowels:
        output_message += input_message[i]

print("Output: " + output_message)
