dia, open_day_input = input().split(" ")
open_day_input = int(open_day_input)
open_hours,open_minute,open_second = list(map(int,input().split(": ")))

dia2, end_day_input = input().split(" ")
end_day_input = int(end_day_input)
end_hours,end_minute,end_second = list(map(int,input().split(": ")))

total_sec = (end_day_input - open_day_input)*86400 + (end_hours-open_hours)*3600 + (end_minute-open_minute)*60 + (end_second-open_second)

day = total_sec//86400
remaning_day = total_sec % 86400
hour = remaning_day//3600
remaning_hour = remaning_day%3600
minute = remaning_hour//60
second = remaning_hour%60

print(f'{day} dia(s)\n{hour} hora(s)\n{minute} minuto(s)\n{second} segundo(s)')
