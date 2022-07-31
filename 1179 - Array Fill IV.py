list_par = []
list_impar = []
for i in range(15):
    u_input = int(input())

    if len(list_par) == 5:
        for i in range(5):
            print(f'par[{i}] = {list_par[i]}')
        list_par = []

    if len(list_impar) == 5:
        for i in range(5):
            print(f'impar[{i}] = {list_impar[i]}')
        list_impar = []

    if u_input % 2 == 0:
        list_par.append(u_input)

    if u_input % 2 != 0:
        list_impar.append(u_input)

for j in range(len(list_impar)):
    print(f'impar[{j}] = {list_impar[j]}')

for j in range(len(list_par)):
    print(f'par[{j}] = {list_par[j]}')
