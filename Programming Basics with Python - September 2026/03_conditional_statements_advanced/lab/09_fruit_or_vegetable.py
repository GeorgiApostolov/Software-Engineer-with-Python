input_fruits_or_veg = input()

if input_fruits_or_veg in ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]:
    print("fruit")
elif input_fruits_or_veg in ["tomato", "cucumber", "pepper", "carrot"]:
    print("vegetable")
else:
    print("unknown")