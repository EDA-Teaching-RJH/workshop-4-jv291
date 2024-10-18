def coffee_mechine():
    total_inserted = 0
    amount_due = 75
    accept_coins = (50, 20, 10, 5)
    while total_inserted < amount_due:
        coin = int(input(f"Please insert a coin"))
        if coin in accept_coins:
            total_inserted += coin
            if total_inserted < amount_due:
                print(f"Amount due: {amount_due - total_inserted}p")
            else:
                change = total_inserted - amount_due
                print(f"Enjoy your coffee. Your change is {change}p")
                break

coffee_mechine()

