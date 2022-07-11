user_input = int(input())
counter = 0

for i in range(user_input, user_input+50):
    if counter !=6:
        if i%2 != 0:
            counter+=1
            print(i)
