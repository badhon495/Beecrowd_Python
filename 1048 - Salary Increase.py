salary_input = float(input())


def count(old, increase):
    new = old * (increase / 100)
    print(f'Novo salario: {"%.2f" % (old + new)}\nReajuste ganho: {"%.2f" %new}\nEm percentual: {increase} %')


if 0 < salary_input <= 400:
    count(salary_input, 15)

elif 400 < salary_input <= 800:
    count(salary_input, 12)

elif 800 < salary_input <= 1200:
    count(salary_input, 10)

elif 1200 < salary_input <= 2000:
    count(salary_input, 7)

elif salary_input > 2000:
    count(salary_input, 4)
