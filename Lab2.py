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
    return lowest, highest


def sort_temperature(in_list):
    out_list = sorted(in_list)
    return out_list

def calc_median_temperature(in_list):
    sort_list = sorted(in_list)
    if len(sort_list)%2 == 0:
        num = int(len(sort_list)/2)
        my_median = (sort_list[num]+sort_list[num-1])/2
    elif len(sort_list)%2 == 1:
        num = len(sort_list)//2
        my_median = sort_list[num]
    return my_median

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(f"Average Temperature: {calc_average(num_list):.2f}")
    print(f"Median Temperature: {calc_median_temperature(num_list):.2f}")
    print(f"Maximum Temperature: {find_min_max(num_list)[0]:.2f}")
    print(f"Minimum Temperature: {find_min_max(num_list)[1]:.2f}")
    print(f"Sorted List: {sort_temperature(num_list)}")

if __name__ == "__main__":
    main()
