# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y

num = 9
a = 6
b = 7
age = 25
temp = 30
user_role = input("Enter your role (admin/guest): ").lower()

# print("Positive"  if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18  else "Child"
# weather = "HOT" if temp > 20 else "COLD"
access_level = "Full access" if user_role == "admin" else "Limited access"

print(access_level)
