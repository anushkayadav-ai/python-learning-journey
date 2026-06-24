# collection = single "variable" used to store multiple values 
#   List = [] ordered and changeable. Duplicates OK
#   Set = {} unordered and mutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ("mango", "orange", "banana", "coconut", "coconut")
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
print("mango" in fruits)   # The 'in' operator checks whether a value exists in the collection.

# fruits[0] = "pineapple"
# fruits.append("pineapple")      # append used to element to the last
# fruits.remove("mango")
# fruits.insert(0, "pineapple")
# fruits.sort()       # sort - arrange in alphabetical order
# fruits.reverse()
# fruits.clear()
# print(fruits.index("mango"))
print(fruits.count("coconut"))
# fruits.add("pineapple")
# fruits.pop()

# print(fruits)
for fruit in fruits:
    print(fruit)