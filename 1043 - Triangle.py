x, y, z = input().split(" ")
x = float(x)
y = float(y)
z = float(z)

original_order = [x, y, z]
ascending_order = sorted(original_order)

if ascending_order[0]+ascending_order[1] > ascending_order[2]:
    print(f'Perimetro = {"%.1f" %(x+y+z)}')
else:
    print(f'Area = {"%.1f" %(((x+y)/2)*z)}')
