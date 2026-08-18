pens_packets = int(input())
markers_packets = int(input())
clear_liters = int(input())
percent_discount = int(input())

total_sum = (pens_packets * 5.80) + (markers_packets * 7.20) + (clear_liters * 1.20)
final_sum = total_sum - (total_sum * (percent_discount / 100))
print(final_sum)