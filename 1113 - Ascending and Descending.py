while True:
    m, n = list(map(int, input().split(" ")))
    if m > n:
        print("Decrescente")
    elif m < n:
        print("Crescente")
    else:
        break
