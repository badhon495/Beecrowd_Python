x = input().lower()
y = input().lower()
z = input().lower()

if x == "vertebrado" and y == "ave" and z == "carnivoro":
    print("aguia")

elif x == "vertebrado" and y == "ave" and z == "onivoro":
    print("pomba")

elif x == "vertebrado" and y == "mamifero" and z == "onivoro":
    print('homem')

elif x == "vertebrado" and y == "mamifero" and z == "herbivoro":
    print('vaca')

elif x == "invertebrado" and y == "inseto" and z == "hematofago":
    print('pulga')

elif x == "invertebrado" and y == "inseto" and z == "herbivoro":
    print('lagarta')

elif x == "invertebrado" and y == "anelideo" and z == "hematofago":
    print("sanguessuga")

elif x == "invertebrado" and y == "anelideo" and z == "onivoro":
    print("minhoca")
