def calculate_bmi(weight, height):
    print(f"Height = {height}")
    print(f"Weight = {weight}")
    bmi = round(weight/(height**2), 2)
    print(f"Your bmi is: {bmi}")
    if bmi < 18.5:
        print("You are underweight")
        return -1
    elif 18.5 <= bmi <= 25.0:
        print("You have a normal weight")
        return 0
    else:
        print("You are overweight")
        return 1

calculate_bmi(weight= 90, height= 1.73)