print("Amount Due: 50")

amount_due = 50

coins_total = 0

while True:

    inserted_coin = int(input("Insert coin: "))

    if inserted_coin == 5 or inserted_coin == 10 or inserted_coin == 25:
        amount_due -= inserted_coin
        coins_total += inserted_coin
    else:
        print("Amount Due:", amount_due)

    if coins_total >= 50:
        print("Change Owed:", (coins_total - 50))
        break
    else:
         print("Amount Due:", amount_due)
