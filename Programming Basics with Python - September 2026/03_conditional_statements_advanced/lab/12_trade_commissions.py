city_input = input()
sales_input = float(input())

if city_input == "Sofia":
    if sales_input > 0 and sales_input <= 500:
        print(f"{(sales_input * 0.05):.2f}")
    elif sales_input >500 and sales_input <= 1000:
        print(f"{(sales_input * 0.07):.2f}")
    elif sales_input > 1000 and sales_input <= 10000:
        print(f"{(sales_input * 0.08):.2f}")
    elif sales_input > 10000:
        print(f"{(sales_input * 0.12):.2f}")
    else:
        print("error")
elif city_input == "Varna":
    if sales_input > 0 and sales_input <= 500:
        print(f"{(sales_input * 0.045):.2f}")
    elif sales_input >500 and sales_input <= 1000:
        print(f"{(sales_input * 0.075):.2f}")
    elif sales_input > 1000 and sales_input <= 10000:
        print(f"{(sales_input * 0.10):.2f}")
    elif sales_input > 10000:
        print(f"{(sales_input * 0.13):.2f}")
    else:
        print("error")
elif city_input == "Plovdiv":
    if sales_input > 0 and sales_input <= 500:
        print(f"{(sales_input * 0.055):.2f}")
    elif sales_input >500 and sales_input <= 1000:
        print(f"{(sales_input * 0.08):.2f}")
    elif sales_input > 1000 and sales_input <= 10000:
        print(f"{(sales_input * 0.12):.2f}")
    elif sales_input > 10000:
        print(f"{(sales_input * 0.145):.2f}")
    else:
        print("error")
else:
    print("error")