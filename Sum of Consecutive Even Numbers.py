x = 1
total = 0
while x != 0:
    x = int(input())
    if x == 0:
        break

    elif x % 2 == 0:
        total = 0
        for j in range(0, 5):
            total += x
            x += 2

    else:
        x += 1
        total = 0
        for j in range(5):
            total += x
            x += 2
    print(total)
