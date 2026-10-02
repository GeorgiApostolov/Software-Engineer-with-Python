dict_type = {
    "Premiere": 12.00,
    "Normal": 7.50,
    "Discount": 5.00
}

type_input = input()
r_input = int(input())
c_input = int(input())
output_result = dict_type[type_input] * r_input * c_input

print(f"{output_result:.2f}")