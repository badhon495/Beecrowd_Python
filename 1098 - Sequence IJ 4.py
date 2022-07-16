i = 0

while True:
    j = 1
    j_temp = j+(i-0)
    if i <= 2:
        for k in range(3):
            if i == 2 or i==1 or i == 0:
                print(f'I={int(i)} J={int(j_temp)}')
            else:
                print(f'I={"%.1f" %i} J={"%.1f" %j_temp}')
            j_temp += 1
    else:
        exit()
    i += 0.2
    i = round(i,2)
