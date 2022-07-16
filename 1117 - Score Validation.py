count = 0
total = 0
while True:
    if count == 2:
        break

    else:
        u_input = float(input())
        if 0 > u_input or 10 < u_input:
            print("nota invalida")
        else:
            total += u_input
            count += 1

print(f'media = {"%.2f" % (total / 2)}')
