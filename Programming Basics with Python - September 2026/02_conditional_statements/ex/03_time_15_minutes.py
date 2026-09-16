input_hours = int(input())
input_minutes = int(input())

input_minutes += 15

while input_minutes >= 60:
    if input_minutes >= 60:
        input_minutes -= 60
        input_hours += 1
    if input_hours == 24:
        input_hours = 0

if input_minutes >= 10:
    print(f"{input_hours}:{input_minutes}")
else:
    print(f"{input_hours}:0{input_minutes}")