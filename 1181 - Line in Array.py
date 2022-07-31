which_row = int(input())
what_to_do = str(input())
list1 = []

for i in range(12):
    temp_list = []
    for j in range(12):
        u_input = input()
        temp_list.append(u_input)

    list1.append(temp_list)

total = 0
for i in list1[which_row]:
    total += int(i)

if what_to_do.upper() == "S":
    print(total)
else:
    print(total / 12)
