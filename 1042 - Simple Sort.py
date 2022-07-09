x, y, z = input().split(" ")
x = int(x)
y = int(y)
z = int(z)

original_order = [x, y, z]
string_original_order = [str(i) for i in original_order]
ascending_order = sorted(original_order)
string_ascending_order = [str(i) for i in ascending_order]

print("\n".join(string_ascending_order))
print()
print("\n".join(string_original_order))
