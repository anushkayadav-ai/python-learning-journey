# List comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

doubles = [x * 2 for x in range(1, 11)]
triples = [x * 3 for x in range(3, 67)]
squares = [z * z for z in range(4, 100)]

print(squares)

fruits = ["apple", "mango", "blueberry", "dates"]
fruit_chars = [fruit.upper() for fruit in fruits]
print(fruit_chars)

numbers = [1, -2, 3, -4, 5, -6, 8, -11]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num <= 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print(odd_nums)

grades = [85, 42, 79, 32, 96, 59, 63]
passing_grades = [grade for grade in grades if grade >=60]

print(passing_grades)