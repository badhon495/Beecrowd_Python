import math

user_input = input()

a, b, c = user_input.split(" ")
a = float(a)
b = float(b)
c = float(c)

if (b * b - 4 * a * c) < 0 or a == 0:
    print("Impossivel calcular")

else:
    r1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    r2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    print(f'R1 = {round(r1, 5)}')
    print(f'R2 = {round(r2, 5)}')
