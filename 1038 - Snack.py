code, quantity = input().split(" ")

total = 0

if code == "1":
    total += 4

elif code == "2":
    total += 4.50

elif code == "3":
    total += 5

elif code == "4":
    total += 2

elif code == "5":
    total += 1.5

print(f"Total: R$ {'%.2f'%(float(total)*int(quantity))}")
