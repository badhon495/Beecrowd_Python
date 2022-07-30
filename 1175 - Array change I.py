num_list = []
for i in range(20):
    u_input = int(input())
    num_list.append(u_input)

num_list.reverse()

for i in range(20):
    print(f'N[{i}] = {num_list[i]}')
