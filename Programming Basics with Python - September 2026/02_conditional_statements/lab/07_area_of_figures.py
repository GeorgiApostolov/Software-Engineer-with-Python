import math

input_figure = input()
input_num = float(input())
if input_figure == "rectangle" or input_figure == "triangle":
    input_second_num = float(input())

if input_figure == "square":
    print(input_num *  input_num)
elif input_figure == "rectangle":
    print(input_num * input_second_num)
elif input_figure == "circle":
    print(math.pi * (input_num ** 2))
elif input_figure == "triangle":
    print(0.5 * input_num * input_second_num)