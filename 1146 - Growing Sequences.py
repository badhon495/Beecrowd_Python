while True:

    n = int(input())
    if n != 0:
        temp_list = []

        for i in range(1, n + 1):
            temp_list.append(str(i))

        print(" ".join(temp_list))

    else:
        break
