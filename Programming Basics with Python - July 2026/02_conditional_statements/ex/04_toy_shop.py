# puzel 2.60 , govoreshta kukla 3 , plusheno meche 4.10 , minion 8.20 , kamionche 2

price = float(input())
count_puzzles = int(input())
count_talking_doll = int(input())
count_teddy_bears = int(input())
count_minions = int(input())
count_trucks = int(input())

sum_puzzles = count_puzzles * 2.60
sum_talking_dolls = count_talking_doll * 3
sum_teddy_bears = count_teddy_bears * 4.10
sum_minions = count_minions * 8.20
sum_trucks = count_trucks * 2

total_sum = sum_puzzles + sum_talking_dolls + sum_teddy_bears + sum_minions + sum_trucks
total_count = count_puzzles + count_talking_doll + count_teddy_bears + count_minions + count_trucks

if total_count >= 50:
    total_sum -= total_sum * 0.25
total_sum -= total_sum * 0.10

if total_sum - price >= 0:
    final = total_sum - price
    print(f"Yes! {final:.2f} lv left.")
else:
    final = price - total_sum
    print(f"Not enough money! {final:.2f} lv needed.")