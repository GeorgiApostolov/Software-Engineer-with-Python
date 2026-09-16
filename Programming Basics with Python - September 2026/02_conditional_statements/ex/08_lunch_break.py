import  math

serial_name = input()
length_ep = int(input())
length_break = int(input())

time_lunch = float(length_break / 8)
time_spa = float(length_break / 4)

final = float(length_break - time_lunch - time_spa)

if final >= length_ep:
    print(f"You have enough time to watch {serial_name} and left with {math.ceil(final - length_ep)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {math.ceil(length_ep - final)} more minutes.")

