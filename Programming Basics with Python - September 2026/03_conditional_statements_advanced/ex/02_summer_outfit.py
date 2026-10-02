degrees_input = int(input())
day_time_input = input()
outfit = ""
shoes = ""


if day_time_input == "Morning":
    if degrees_input >= 10 and degrees_input <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif degrees_input > 18 and degrees_input <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif degrees_input >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif day_time_input == "Afternoon":
    if degrees_input >= 10 and degrees_input <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif degrees_input > 18 and degrees_input <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif degrees_input >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
elif day_time_input == "Evening":
    if degrees_input >= 10 and degrees_input <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif degrees_input > 18 and degrees_input <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif degrees_input >= 25:
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {degrees_input} degrees, get your {outfit} and {shoes}.")