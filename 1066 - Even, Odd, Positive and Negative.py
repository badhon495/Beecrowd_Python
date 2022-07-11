even_counter = 0
odd_counter = 0
positive_counter = 0
negative_counter = 0

for i in range(1, 6):
    user_input = int(input())
    if user_input % 2 == 0:
        even_counter += 1
    if user_input % 2 != 0:
        odd_counter += 1
    if user_input < 0:
        negative_counter += 1
    if user_input > 0:
        positive_counter += 1

print(f'{even_counter} valor(es) par(es)\n{odd_counter} valor(es) impar(es)\n{positive_counter} valor(es) positivo(s)\n{negative_counter} valor(es) negativo(s)')
