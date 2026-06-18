# logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be true 
#                     and =both conditions must be true
#                     not = inverts the condition (not False, not True)


# temp = 34
# is_raining = False

# if temp > 35 or is_raining or temp < 0 :
#     print("The outdoor event is cancelled")
# else: 
#     print("The outdoor event is still scheduled")


temp = float(input("Enter the temperature: "))
is_sunny = input("Is it sunny? (Y/N): ").upper() == "Y"

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is CLOUDY")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside")
    print("It is CLOUDY")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside")
    print("It is CLOUDY")

