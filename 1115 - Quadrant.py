while True:
    m, n = list(map(int, input().split(" ")))

    if m > 0 and n > 0:
        print("primeiro")

    elif m > 0 and n < 0:
        print("quarto")
    elif m < 0 and n < 0:
        print("terceiro")
    elif m < 0 and n > 0:
        print("segundo")
    else:
        break
