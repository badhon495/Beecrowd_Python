start = int(input())
end = int(input())
sum = 0

if end<start:
    if end<0:
        for i in range(end+1, start, 1):
            if i % 2 != 0:
                sum += i
    else:
        for i in range(end, start, 1):
            if i % 2 != 0:
                sum += i
else:
    for i in range(start, end+1, 1):
        if i % 2 != 0:
            sum += i
print(sum)
