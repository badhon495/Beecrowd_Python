while True:
    m, n = sorted(list(map(int, input().split(" "))))
    total = 0
    if m <= 0 or n <= 0:
        break
    for i in range(m, n + 1):
        print(i, end=" ")
        total += i
    print(f'Sum={total}')
