positive_counter = 0

for i in range(1, 7):
    user_input = float(input())
    if user_input > 0:
        positive_counter += 1

print(f'{positive_counter} valores positivos')
