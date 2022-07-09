x, y, z = input().split(" ")

x = float(x)
y = float(y)
z = float(z)

order = [x, y, z]

decreasing_code = sorted(order, reverse=True)
a = decreasing_code[0]
b = decreasing_code[1]
c = decreasing_code[2]

if a >= b + c:
    print("NAO FORMA TRIANGULO")
    exit()
if a * a == (b * b + c * c):
    print("TRIANGULO RETANGULO")
if a * a > (b * b + c * c):
    print("TRIANGULO OBTUSANGULO")
if a * a < (b * b + c * c):
    print("TRIANGULO ACUTANGULO")
if a == b == c:
    print("TRIANGULO EQUILATERO")
if (a == b and a != c) or (b == c and a != b) or (a == c and a != b):
    print("TRIANGULO ISOSCELES")
