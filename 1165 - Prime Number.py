n = int(input())

for i in range(n):
    u_input = int(input())
    flag = True
    for j in range(2, u_input):
        if u_input % j == 0:
            flag = False
            break
        else:
            flag = True

    if flag is False:
        print(f'{u_input} nao eh primo')
    else:
        print(f'{u_input} eh primo')
