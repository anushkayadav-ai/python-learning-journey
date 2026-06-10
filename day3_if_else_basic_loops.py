
x = 3.14
y = 4
z = 5

# result = round(x)
# result = abs(y)
# result = pow(4, 3)
# result = max(x, y, z)
result = min(x, y, z)

print(result)


import math 

x = 9.9
print(math.pi)
print(math.e)
# result = math.sqrt(x)
# result = math.ceil(x)
result = math.floor(x)

print(result)

radius = float(input('Enter the radius of a circle: '))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm ")


radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)
print(f"The area of the circle is: {round(area, 3)}cm^2")

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
          
c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c}")

# if = Do some code only IF some condition is True
#     Else do something else


age = int(input("Enter your age: "))

if age >= 100: 
 print("You are too old to sign up!")
elif age >= 18:
   print("You are now signed up! ")
elif age < 0:
    print("You haven't been born yet!")
else: 
    print("You must be 18+ to sign up")

response = input("Would you like food? (Y/N): ").upper()
 
if response == "Y":
   print("Have some food!") 
elif response == "N":
   print("No food for you!")
else: 
 print("Please enter Y or N")