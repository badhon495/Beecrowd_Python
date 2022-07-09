user_input = float(input())

if 0 > user_input or 100 < user_input:
    print("Fora de intervalo")

elif 0 <= user_input <= 25:
    print("Intervalo [0,25]")

elif 25 < user_input <= 50:
    print("Intervalo (25,50]")

elif 50 < user_input <= 75:
    print("Intervalo (50,75]")

elif 75 < user_input <= 100:
    print("Intervalo (75,100]")
