first_input = int(input())
second_input = int(input())
third_input = int(input())

seconds_sum = first_input + second_input + third_input
minutes = seconds_sum // 60
seconds = seconds_sum % 60

if seconds >= 10:
    print(f"{minutes}:{seconds}")
else:
    print(f"{minutes}:0{seconds}")