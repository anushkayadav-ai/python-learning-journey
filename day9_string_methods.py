
# name = input("Enter ypur full name: ")
phone_number = input("Enter your phone #: ")

# result = len(name)  
# result = name.find("U")
# result = name.rfind("v")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()  # only contains digit
# result = name.isalpha()    # contains only alphabetical orders

# result = phone_number.count("-")
phone_number =  phone_number.replace("-", "*")


print(phone_number)

# print(help(str))

## Exercise

# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")



if len(username) > 12:
    print("Your username can't be more than 12 characters ")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain digits")
else:
    print(f"Welcome {username}")