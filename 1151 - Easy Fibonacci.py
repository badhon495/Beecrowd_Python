n = int(input())

first_value = 0
second_value = 1
next_value = 0
count = 3
list1 = [str(first_value),str(second_value)]

while count <= n:
    next_value = first_value+second_value
    list1.append(str(next_value))
    first_value = second_value
    second_value = next_value
    count+=1

print(" ".join(list1))
