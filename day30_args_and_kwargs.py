# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments
#            * unpacking operator
#            1. positional 2. default 3. keyword 4. ARBITRARY

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4, 5, 6))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Anushka", "Satoria", "Yadav")


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.",
              apt="100", 
              city="Detroit", 
              state="MI", 
              zip="54321")


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ") 
    print()
#     for value in kwargs.values():
#         print(value, end=" ")
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "PObox" in kwargs:
         print(f"{kwargs.get('street')}")
         print(f"{kwargs.get('PObox')}")
    else:
         print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake St.",
               PObox="PO box #1001", 
               city="Detroit", 
               state="MI", 
               zip="54321")


def student_info(**kwargs):
    for info in kwargs:
        print(info)

student_info = (name = "Anushka", 
                age = "16", 
                country = "India", 
                goal = "AI Engineer")