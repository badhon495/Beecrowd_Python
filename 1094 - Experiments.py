total_animal_count = 0
coelho = 0
rato = 0
sapo = 0
n = int(input())

for i in range(n):
    number, name = input().split(" ")

    number = int(number)
    total_animal_count+= number

    if name == "C":
        coelho+=number
    elif name == 'R':
        rato+=number
    else:
        sapo+=number

coelho_rate = (coelho/total_animal_count)*100
rato_rate = (rato/total_animal_count)*100
sapo_rate = (sapo/total_animal_count)*100

print(f'Total: {total_animal_count} cobaias\nTotal de coelhos: {coelho}\nTotal de ratos: {rato}\nTotal de sapos: {sapo}\nPercentual de coelhos: {"%.2f" %coelho_rate} %\nPercentual de ratos: {"%.2f" %rato_rate} %\nPercentual de sapos: {"%.2f" %sapo_rate} %')
