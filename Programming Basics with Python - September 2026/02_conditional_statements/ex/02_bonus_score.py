input_num = int(input())
points = 0
if input_num <= 100:
    points += 5
elif input_num <= 1000:
    points += input_num*0.20
else:
    points += input_num*0.10

if input_num % 2 == 0:
    points += 1
if input_num % 10 == 5:
    points += 2
print(points)
print(input_num + points)