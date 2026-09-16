deposit_sum_input = float(input())
deadline_input = int(input())
annual_interest_rate = float(input())

final_sum = deposit_sum_input + deadline_input * ((deposit_sum_input* (annual_interest_rate / 100) ) / 12)
print(final_sum)