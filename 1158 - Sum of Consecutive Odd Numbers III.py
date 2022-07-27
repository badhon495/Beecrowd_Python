n = int(input())
total = 0
count = 0
for i in range(n):
    x, y = list(map(int, input().split(" ")))
    if x % 2 == 1:
        total = 0
        for j in range(0, y):
            total += x
            x += 2

    else:
        x += 1
        total = 0
        for j in range(y):
            total += x
            x += 2
    print(total)
