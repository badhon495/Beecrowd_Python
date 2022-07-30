n = int(input())

for i in range(n):
    count = 0
    small, big, small_g, big_g = input().split(" ")
    small = int(small)
    big = int(big)
    small_g = float(small_g)
    big_g = float(big_g)

    while True:
        if small > big:
            if count > 100:
                print(f'Mais de 1 seculo.')
                break
            else:
                print(f'{count} anos.')
                break
        else:
            big = big + int(big * (big_g / 100))
            small = small + int(small * (small_g / 100))
            count += 1
            if count > 100:
                print(f'Mais de 1 seculo.')
                break
