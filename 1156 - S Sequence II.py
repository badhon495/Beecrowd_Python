total = 1
count = 1

for i in range(3,40,2):
    total += i/(2**count)
    count+=1

print("%.2f" % total)
