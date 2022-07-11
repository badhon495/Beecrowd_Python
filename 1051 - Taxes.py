money = float(input())

if 0 < money <= 2000:
    print(f"Isento")

elif 2000 < money <= 3000:
    money_left = money - 2000
    tax = money_left * 0.08
    print(f"R$ {tax:0.2f}")

elif 3000 < money < 4500:
    money_left = money - 3000
    tax = (money_left * 0.18) + (1000 * 0.08)
    print(f"R$ {tax:0.2f}")

else:
    money_left = money - 4500
    tax = (money_left * 0.28) + (1500 * 0.18) + (1000 * 0.08)
    print(f"R$ {tax:0.2f}")
