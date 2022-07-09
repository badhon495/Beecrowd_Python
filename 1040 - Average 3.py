n1, n2, n3, n4 = input().split(" ")

n1 = float(n1) * 2
n2 = float(n2) * 3
n3 = float(n3) * 4
n4 = float(n4)

avg = (n1 + n2 + n3 + n4) / 10
print(f'Media: {"%.1f" % avg}')


def count1(number):
    if number >= 5:
        print("Aluno aprovado.")
    elif number < 5:
        print("Aluno reprovado.")


def count(number):
    if number >= 7:
        print("Aluno aprovado.")
    elif number < 5:
        print("Aluno reprovado.")
    elif 5 <= number <= 6.9:
        print("Aluno em exame.")
        extra_input = input()
        new_avg = (avg + float(extra_input)) / 2
        print(f'Nota do exame: {"%.1f" % (float(extra_input))}')
        count1(new_avg)
        print(f'Media final: {"%.1f" % new_avg}')


count(avg)
