u_input = int(input())
count = 0
while count < 1000:
    for j in range(u_input):
        if count < 1000:
            print(f'N[{count}] = {j}')
            count += 1
