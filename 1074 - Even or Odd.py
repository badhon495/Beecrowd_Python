input_number = int(input())
count = 0

while count != input_number:
    user_input = int(input())
    count+=1
    if user_input == 0:
        print("NULL")
    elif user_input % 2 == 0 and user_input > 0:
        print("EVEN POSITIVE")
    elif user_input % 2 != 0 and user_input > 0:
        print("ODD POSITIVE")
    elif user_input % 2 != 0 and user_input < 0:
        print("ODD NEGATIVE")
    elif user_input % 2 == 0 and user_input < 0:
        print("EVEN NEGATIVE")
