positive_counter = 0
positive_sum = 0

for i in range(1, 7):
    user_input = float(input())
    if user_input > 0:
        positive_counter += 1
        positive_sum+=user_input

print(f'{positive_counter} valores positivos')
print(format(positive_sum/positive_counter, ".1f"))
