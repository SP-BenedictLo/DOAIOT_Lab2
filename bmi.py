def calculate_bmi(height, weight):
    print(f"Height = {height}")
    print(f"Weight = {weight}")
    bmi = round(weight/height**2, 2)
    print(f"Your bmi is: {bmi}")
    if bmi < 18.5:
        print("You are underweight")
    elif 18.5 <= bmi <= 25.0:
        print("You have a normal weight")
    else:
        print("You are overweight")

calculate_bmi(weight= 57, height= 1.73)