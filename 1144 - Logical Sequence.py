n = int(input())
run = 0
count = 1

while run < (n * 2):
    print(f'{count} {count ** 2} {count ** 3}')
    print(f'{count} {(count ** 2) + 1} {(count ** 3) + 1}')
    count += 1
    run += 2
