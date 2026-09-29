length_tank = int(input())
width_tank = int(input())
height_tank = int(input())
percent = float(input())

aquarium_volume = length_tank * width_tank * height_tank
volume_litre = aquarium_volume * 0.001
occupied_space = percent / 100

needs_litre = volume_litre * (1 - occupied_space)

print(needs_litre)