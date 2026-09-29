#град / продукт	coffee	water	beer	sweets	peanuts
#Sofia	0.50	0.80	1.20	1.45	1.60
#Plovdiv	0.40	0.70	1.15	1.30	1.50
#Varna	0.45	0.70	1.10	1.35	1.55

product_input = input()
town_input = input()
count_input = float(input())

if town_input == "Sofia":
    if product_input == "coffee":
        print(float(count_input * 0.50))
    elif product_input == "water":
        print(float(count_input * 0.80))
    elif product_input == "beer":
        print(float(count_input * 1.20))
    elif product_input == "sweets":
        print(float(count_input * 1.45))
    elif product_input == "peanuts":
        print(float(count_input * 1.60))
elif town_input == "Plovdiv":
    if product_input == "coffee":
        print(float(count_input * 0.40))
    elif product_input == "water":
        print(float(count_input * 0.70))
    elif product_input == "beer":
        print(float(count_input * 1.15))
    elif product_input == "sweets":
        print(float(count_input * 1.30))
    elif product_input == "peanuts":
        print(float(count_input * 1.50))
elif town_input == "Varna":
    if product_input == "coffee":
        print(float(count_input * 0.45))
    elif product_input == "water":
        print(float(count_input * 0.70))
    elif product_input == "beer":
        print(float(count_input * 1.10))
    elif product_input == "sweets":
        print(float(count_input * 1.35))
    elif product_input == "peanuts":
        print(float(count_input * 1.55))