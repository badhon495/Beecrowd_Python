x = int(input())
z = int(input())
count = 0
total = 0
while z <= x:
    z = int(input())

while total < z:
    total += x
    x += 1
    count += 1

print(count)
