camelCase = input("camelCase: ").strip()

snake_case = ""

for i in range(len(camelCase)):
    if camelCase[i].islower():
        snake_case += camelCase[i]
    else:
        snake_case = snake_case + '_' + camelCase[i].lower()

print("snake_case: " + snake_case)
