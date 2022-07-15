i = 1
j = 7
while i <= 9:
    temp = j
    temp_x = j-2

    while temp >= temp_x:
        print(f'I={i} J={temp}')
        temp -= 1
    j += 2
    i += 2
