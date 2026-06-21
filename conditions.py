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