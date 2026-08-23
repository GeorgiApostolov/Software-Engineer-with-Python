budget = float(input())
count_statist = int(input())
price_clothes = float(input())
decor = budget * 0.10

final_price_clothes = price_clothes * count_statist

if count_statist >= 150:
    final_price_clothes -= final_price_clothes * 0.10

final_price = final_price_clothes + decor

if budget < final_price:
    final = final_price - budget
    print(f"Not enough money!")
    print(f"Wingard needs {final:.2f} leva more.")
else:
    final = budget - final_price
    print(f"Action!")
    print(f"Wingard starts filming with {final:.2f} leva left.")

