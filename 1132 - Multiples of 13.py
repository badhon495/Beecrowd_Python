x = int(input())
y = int(input())
sum = 0

if x < y:
    for i in range(x, y + 1):
        if i % 13 != 0:
            sum += i
else:
    for i in range(y, x + 1):
        if i % 13 != 0:
            sum += i
print(sum)
