peter_budget = float(input())
count_video_cards = int(input())
count_proccesors = int(input())
count_ram = int(input())
sum = 0

sum += (count_video_cards * 250) + (((count_video_cards * 250) * 0.35) * count_proccesors) + (((count_video_cards * 250) * 0.10) * count_ram)

if count_video_cards > count_proccesors:
    sum -= sum * 0.15

if peter_budget >= sum:
    print(f"You have {peter_budget - sum:.2f} leva left!")
else:
    print(f"Not enough money! You need {sum-peter_budget:.2f} leva more!")