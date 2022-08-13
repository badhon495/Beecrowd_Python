caw = 0
count = 0
while caw < 3:
    u_input = str(input())

    if u_input == "caw caw":
        print(count)
        caw += 1
        count = 0

    else:

        for i in range(3):
            if u_input[i:i + 1] == "*":
                if i == 0:
                    count += 4
                elif i == 1:
                    count += 2
                else:
                    count += 1

