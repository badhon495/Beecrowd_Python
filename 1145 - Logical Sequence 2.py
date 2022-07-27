x, y = list(map(int, input().split(" ")))

count = 1
for i in range(1, y):
    if count <= y:
        temp_list = []
        for j in range(x):
            temp_list.append(str(count+j))
        print(" ".join(temp_list))
        count += x
