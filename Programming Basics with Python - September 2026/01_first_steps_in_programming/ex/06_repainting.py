nylon = int(input())
paint = int(input())
thinner = int(input())
hours_work = int(input())

total_nylon = (nylon + 2) * 1.50
total_paint = (paint + (paint * 0.10))  * 14.50
total_thinner = thinner * 5.00
total_sum_materials = total_nylon + total_paint + total_thinner + 0.40
workers_sum = (total_sum_materials * 0.30) * hours_work
print(total_sum_materials + workers_sum)