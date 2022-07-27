n =int(input())
total = 0
count = 0
while n>0:
    total+=n
    count += 1
    n= int(input())


print("%.2f"%(total/count))
