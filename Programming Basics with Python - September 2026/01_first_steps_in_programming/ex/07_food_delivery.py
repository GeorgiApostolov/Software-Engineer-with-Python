chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())
total_price = float((chicken_menu * 10.35) + (fish_menu * 12.40) + (vegetarian_menu * 8.15))
desert = total_price * 0.20
total_price += desert
delivery = 2.50
total_price += delivery
print(total_price)
