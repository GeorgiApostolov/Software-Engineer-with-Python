work_days = {
    "banana": 2.50,
    "apple": 1.20,
    "orange": 0.85,
    "grapefruit": 1.45,
    "kiwi": 2.70,
    "pineapple": 5.50,
    "grapes": 3.85
}

weekend_days = {
    "banana": 2.70,
    "apple": 1.25,
    "orange": 0.90,
    "grapefruit": 1.60,
    "kiwi": 3.00,
    "pineapple": 5.60,
    "grapes": 4.20
}

fruit_input = input()
day_input = input()
count_input = float(input())

if day_input in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    if fruit_input in ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]:
        result_print = work_days[fruit_input] * count_input
        print(f"{round(result_print, 2):.2f}")
    else:
        print("error")
elif day_input in ["Saturday", "Sunday"]:
    if fruit_input in ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]:
        result_print = weekend_days[fruit_input] * count_input
        print(f"{round(result_print, 2):.2f}")
    else:
        print("error")
else:
    print("error")