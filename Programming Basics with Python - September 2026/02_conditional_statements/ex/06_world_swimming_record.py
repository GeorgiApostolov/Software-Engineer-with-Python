import math

records_seconds = float(input())
distance_metres = float(input())
time_seconds_for_one_meter = float(input())

swimming_time = distance_metres * time_seconds_for_one_meter
bonus = math.floor(distance_metres / 15) * 12.5

final = swimming_time + bonus

if final < records_seconds:
    print(f"Yes, he succeeded! The new world record is {final:.2f} seconds.")
else:
    distract = final - records_seconds
    print(f"No, he failed! He was {distract:.2f} seconds slower.")