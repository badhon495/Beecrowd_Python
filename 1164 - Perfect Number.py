n = int(input())

for i in range(n):
    u_input = int(input())
    total = 0

    for j in range(1, u_input):
        if u_input % j == 0:
            total += j

    if total == u_input:
        print(f'{u_input} eh perfeito')
    else:
        print(f'{u_input} nao eh perfeito')
