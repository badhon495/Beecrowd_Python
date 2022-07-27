temp_list = list(map(int, input().split(" ")))

a = temp_list[0]
n = 0
total = 0
count = 0

for i in temp_list[1::]:
    if i > 0:
        n = i
        break

while count != n:
    total += a
    a += 1
    count += 1


print(total)
