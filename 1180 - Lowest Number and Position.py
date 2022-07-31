u_input = int(input())
list1 = list(map(int,input().split()))

small_digit = list1[0]
small_digit_index = 0

for i in range(u_input):
    if list1[i] < small_digit:
        small_digit = list1[i]
        small_digit_index = i

print(f'Menor valor: {small_digit}\nPosicao: {small_digit_index}')
