n = int(input())

for i in range(n):
    total = 0
    num1, num2 = sorted(list(map(int, input().split(" "))))

    for j in range(num1 + 1, num2):
        if j % 2 != 0:
            total += j
    print(total)
