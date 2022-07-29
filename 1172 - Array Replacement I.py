list1 = []

while len(list1) < 10:
    u_input = int(input())

    if u_input ==0 or u_input<0:
        list1.append(1)
    else:
        list1.append(u_input)


for i in range(10):
    print(f'X[{i}] = {list1[i]}')
