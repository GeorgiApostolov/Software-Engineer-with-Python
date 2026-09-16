input_animal = input()

if input_animal == "dog":
    print("mammal")
elif input_animal == "crocodile" or input_animal == "tortoise" or input_animal == "snake":
    print("reptile")
else:
    print("unknown")