start, end = input().split(" ")

start = int(start)
end = int(end)

if start/10 >= 1 > end/10:
    end+=24
    print(f"O JOGO DUROU {end-start} HORA(S)")
elif start==end :
    print("O JOGO DUROU 24 HORA(S)")
else:
    print(f"O JOGO DUROU {abs(end-start)} HORA(S)")
