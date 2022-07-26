alcohol = 0
gasoline = 0
diesel = 0
while True:
    u_input = int(input())
    if 1 <= u_input <= 4:
        if u_input == 1:
            alcohol += 1
        elif u_input == 2:
            gasoline += 1
        elif u_input == 3:
            diesel += 1
        elif u_input == 4:
            break

    else:
        pass


print("MUITO OBRIGADO")
print(f'Alcool: {alcohol}')
print(f'Gasolina: {gasoline}')
print(f'Diesel: {diesel}')
