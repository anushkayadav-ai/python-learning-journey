# function = A block of resuable code
#            place () after the function name to invoke it

def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print(f"Happy birthday to you!")
    print()

happy_birthday("Anushka", 17)
happy_birthday("Henry", 20)
happy_birthday("Chen Huan'er", 19)


def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Chen Huan'er", 100, "01/02")

# return = statement used to end a function
#          and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(3, 5))
print(subtract(5, 3))
print(multiply(4, 5))
print(divide(10, 5))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("chen", "huan'er")

print(full_name)