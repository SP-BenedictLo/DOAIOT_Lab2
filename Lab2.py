def display_main_menu():
    return "Enter some numbers separated by commas (e.g. 5, 67,32)"

def get_user_input():
    user_input = input("Enter here: ").split(", ")
    user_input = [float(i) for i in user_input]
    return user_input
    

def calc_average(list1):
    avg = 0.0
    sum = 0.0
    for i in list1:
        sum += i 
    avg = round(sum/len(list1), 3)
    return avg 

def find_min_max(in_list):
    if len(in_list) == 1:
        return in_list
    else:
        highest = in_list[1]
        lowest = in_list[0]
    for i in in_list:
        if i > highest:
            highest = i
        elif i < lowest:
            lowest = i
    return (lowest, highest)


def sort_temperature(in_list):
    out_list = sorted(in_list)
    return out_list

def calc_median_temperature(in_list):
    if len(in_list)%2 == 0:
        num = int(len(in_list)/2)
        my_median = (in_list[num]+in_list[num-1])/2
    elif len(in_list)%2 == 1:
        num = len(in_list)//2
        my_median = in_list[num]
    return my_median


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

if __name__ == "__main__":
    main()
