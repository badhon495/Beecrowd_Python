even_counter = 0

for i in range(1, 6):
    user_input = int(input())
    if user_input % 2 == 0:
        even_counter += 1

print(f'{even_counter} valores pares')
