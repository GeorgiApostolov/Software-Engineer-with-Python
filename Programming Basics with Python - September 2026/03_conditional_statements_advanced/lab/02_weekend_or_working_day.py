input_day = input()

if input_day == "Monday" or input_day == "Tuesday" or input_day == "Wednesday" or input_day == "Thursday" or input_day == "Friday":
    print("Working day")
elif input_day == "Saturday" or input_day == "Sunday":
    print("Weekend")
else:
    print("Error")