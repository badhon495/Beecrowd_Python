x,y = input().split(" ")

x = int(x)
y = int(y)

if y%x == 0 or x%y == 0:
    print("Sao Multiplos")

else:
    print("Nao sao Multiplos")
