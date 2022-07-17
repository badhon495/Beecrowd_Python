money, coin = list(map(int, input().split(".")))

# notas
hundred = money / 100
hundred_left = money % 100
fifty = hundred_left / 50
fifty_left = hundred_left % 50
twenty = fifty_left / 20
twenty_left = fifty_left % 20
ten = twenty_left / 10
ten_left = twenty_left % 10
five = ten_left / 5
five_left = ten_left % 5
two = five_left / 2
two_left = five_left % 2


#medas
two_left = coin+(two_left*100)
mul = 100

one = two_left / (1*mul)
one_left = two_left % (1*mul)
point_five = one_left / (.5*mul)
point_five_left = one_left % (.5*mul)
point_twenty_five = point_five_left / (.25*mul)
point_twenty_five_left = point_five_left % (.25*mul)
point_ten = point_twenty_five_left / (.10*mul)
point_ten_left = point_twenty_five_left % (.10*mul)
point_zero_five = point_ten_left / (.05*mul)
point_zero_five_left = point_ten_left % (.05*mul)
point_zero_one = point_zero_five_left / (.01*mul)
point_zero_one_left = point_zero_five_left % (.01*mul)

print(
    f'NOTAS:\n{int(hundred)} nota(s) de R$ 100.00\n{int(fifty)} nota(s) de R$ 50.00\n{int(twenty)} nota(s) de R$ 20.00\n{int(ten)} nota(s) de R$ 10.00\n{int(five)} nota(s) de R$ 5.00\n{int(two)} nota(s) de R$ 2.00')

print(
    f'MOEDAS:\n{int(one)} moeda(s) de R$ 1.00\n{int(point_five)} moeda(s) de R$ 0.50\n{int(point_twenty_five)} moeda(s) de R$ 0.25\n{int(point_ten)} moeda(s) de R$ 0.10\n{int(point_zero_five)} moeda(s) de R$ 0.05\n{int(point_zero_one)} moeda(s) de R$ 0.01')

