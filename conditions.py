# part 1
# step 1
age = int(input("enter your age "))
if age >= 18:
    print("Can enter")
else:
    print("Cannot enter")
# step 2
temperature = 30
if temperature > 37.5:
    print("High temperature")
else:
    print("Normal temperature")
# step 3
number = int(input("enter number to check if it is even "))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
# step 4
battery = 15
is_charging = True
if battery < 20 and is_charging == True:
    print("Low battery, charging now")
elif battery < 20 and is_charging == False:
    print("Low battery, connect charger")
else:
    print("Battery OK")
# step 5
password = input("enter your password to get access ")
if password == "python123":
    print("Access approved")
else:
    print("Access denied")
# step 6
score = 82
if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Good")
elif score >= 60:
    print("Pass")
else:
    print("Fail")
# step 7
first_number = int(input("enter the first number "))
second_number = int(input("enter the second number "))
if first_number > second_number:
    print("First is bigger")
elif first_number < second_number:
    print("Second is bigger")
else:
    print("Equal")
# step 8
fuel = 40
distance = 30
if fuel - distance >= 10:
    print("Enough fuel with reserve")
elif fuel - distance < 10:
    print("Enough fuel, low reserve")
else:
    print("Not enough fuel")
# step 9
username = input("enter your username ")
if username == "":
    print("Guest user")
else:
    print(f"Hello {username}")
# step 10
hour = 10
if hour > 23 or hour < 0:
    print("Invalid hour")
elif hour < 12:
    print("Morning")
elif hour < 18:
    print("Afternoon")
else:
    print("Evening")

# part 2
# step 1
trip_choose = input("where you want to go: forest, cave, or river ")
if trip_choose == "forest":
    hide_or_walk = input("they want to hide or walk ")
    if hide_or_walk == "hide":
        print("You hide behind a tree")
    elif hide_or_walk == "walk":
        print("You find a sleeping wolf")
    else:
        print("Invalid forest action")
elif trip_choose == "cave":
    torch = input("you have a torch by entering yes or no ")
    if torch == "yes":
        left_or_right = input("you want to go left or right ")
        if left_or_right == "left":
            print("You find gold")
        elif left_or_right == "right":
            print("You find bats")
        else:
            print("Invalid cave path")
    elif torch == "no":
        print("It is too dark to enter")
elif trip_choose == "river":
    print("You find a boat")
else:
    print("Unknown place")
# step 2
Calculator_number_first = float(input("enter first number to Calculator "))
Calculator_number_second = float(input("enter second number to Calculator "))
Calculator_action = input("enter an action: add, subtract, or multiply ")
if Calculator_action == "add":
    print(f"your result is {Calculator_number_first + Calculator_number_second}")
elif Calculator_action == "subtract":
    print(f"your result is {Calculator_number_first - Calculator_number_second}")
elif Calculator_action == "multiply":
    print(f"your result is {Calculator_number_first * Calculator_number_second}")
else:
    print("Unknown action")
# step 3
