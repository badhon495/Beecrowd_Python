input_number = int(input())
in_count = 0
out_count = 0

for i in range(input_number):
    user_input = int(input())
    if 10 <= user_input <= 20:
        in_count += 1
    else:
        out_count += 1

print(f'{in_count} in\n{out_count} out')
