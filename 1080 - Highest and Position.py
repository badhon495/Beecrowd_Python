highest_number = 0
highest_number_position = 0

for i in range(1, 101):
    u_input = int(input())

    if u_input > highest_number:
        highest_number = u_input
        highest_number_position = i


print(highest_number)
print(highest_number_position)
