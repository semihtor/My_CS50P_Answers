grocery_list = {}

while True:
    try:
        item = input().upper()
    except (EOFError):
        print()
        break
    if item in grocery_list:
        grocery_list[item] += 1
    else:
        grocery_list[item] = 1

sorted_grocery_list = dict(sorted(grocery_list.items()))

for item in sorted_grocery_list:
    print(sorted_grocery_list[item], item)
