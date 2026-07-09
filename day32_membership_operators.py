# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter not in word:
   print(f"{letter} was not found")
else:
   print(f"There is a {letter}")
   

students = {"Anushka", "Deepika", "Deepanshu", "Vamika"}

student = input(f"Enter the name of a student: ")

if student not in students:
   print(f"{student} was not found")
else:
   print(f"{student} is a student")
   

grades = {"Anushka": "A", 
          "Navya": "B", 
          "Nupur": "C", 
          "Kinjal": "D"}

student = input("Enter the name of a student: ")

if student in grades:
   print(f"{student}'s grade is {grades[student]}")
else:
   print(f"{student} was not found")


email = "yadav.anushkagmail.com"

if "@" in email and "." in email:
   print("Valid email")
else:
   print("Invalid email")