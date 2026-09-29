clock_input = int(input())
day_input = input()
is_open = "closed"

if day_input == "Monday" or day_input == "Tuesday" or day_input == "Wednesday" or day_input == "Thursday" or day_input == "Friday" or day_input == "Saturday":
    if clock_input >= 10 and clock_input<= 18:
        is_open = "open"
        print(is_open)

if is_open == "closed":
    print(is_open)