#•	Баскетболни кецове – цената им е 40% по-малка от таксата за една година
#•	Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
#•	Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
#•	Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка

year_tax_training = int(input())
basketball_sneakers = year_tax_training - (year_tax_training * 0.40)
basketball_outfit = basketball_sneakers - (basketball_sneakers * 0.20)
basketball_ball = basketball_outfit / 4
basketball_accessories = basketball_ball / 5

total = year_tax_training + basketball_sneakers + basketball_outfit + basketball_ball + basketball_accessories
print(total)