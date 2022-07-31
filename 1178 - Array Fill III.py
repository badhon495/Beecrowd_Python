u_input = float(input())
count = 0
for i in range(100):
    print(f'N[{i}] = {"%.4f" %u_input}')
    u_input = u_input/2
