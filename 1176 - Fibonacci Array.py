test_cases = int(input())
for i in range(test_cases):
    u_input = int(input())
    first_digit = 0
    second_digit = 1
    total = 0
    if u_input == 0:
        print(f'Fib(0) = 0')
    elif u_input == 1:
        print(f"Fib({u_input}) = 1")
    else:
        for j in range(0, u_input):
            total = first_digit + second_digit
            first_digit = second_digit
            second_digit = total

        print(f'Fib({u_input}) = {first_digit}')
