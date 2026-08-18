input_speed = float(input())

if input_speed <= 10:
    print("slow")
elif input_speed > 10 and input_speed <= 50:
    print("average")
elif input_speed > 50 and input_speed <= 150:
    print("fast")
elif input_speed > 150 and input_speed <= 1000:
    print("ultra fast")
else:
    print("extremely fast")