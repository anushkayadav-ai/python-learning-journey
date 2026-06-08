#This is my first python program
print("I like Pizza")
print("It's really good")

# Variable = A container for a value (string, integer, float, boolean)
#            A varaiable behaves as if it was the value it contains

# Strings = series of characters they can include numbers but we treat them as characters 
## Strings
first_name = "Anushka"
food = "french fries"
email = "Anushka0709@foodie.com"

print("first_name")
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

# Integers 
age = 16
quantity = 9
num_of_students = 53

print(f"you are {age} years old")
print(f" You are buying {quantity} quantites")
print(f"There are {num_of_students} students in the class")



# Float = A Float is a number , but it conatains a decimal
price = 299.99
gpa = 7.8
distance = 15.7

print(f"The price is ${price}")
print(f"your gpa is: {gpa}")
print(f"You ran {distance} km")


# Boolean 

is_student = False

print(f"Are you a student: {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

for_sale = False

if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT for sale")

is_guaranteed_scholarship = True
if is_guaranteed_scholarship:
    print("You guaranteed your scholarship")
else:
    print("Sorry you are rejected")


# Typecasting = the process of converting a variable from one data type to another str(), int(), float(), bool()

name = "Anushka"
age = 16
gpa = 7.8
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
age = str(age)

print(gpa)
print(type(age))

age += "1"
print(age)

name = bool(name)
print(name)


# input() = A function that prompts thr user to enter data 
#           Returns the entered data as a string

name = input("What is your name?: ")
age = int(input("How old are you?:"))
age = age + 1

print(f"Hello {name}!")
print(f"You are {age} years old")
print("HAPPY BIRTHDAY!")

# Exercise 1 Rectangle Area Calc

length = int(input("Enter the length: "))
widht = int(input("Enter the width: "))

area = length * widht
print(f"The area is: {area} cm²")

# Exercise 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?:"))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s ")
print(f"Your total is ; ${total}")
