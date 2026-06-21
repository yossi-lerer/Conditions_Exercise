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