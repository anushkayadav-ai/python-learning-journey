# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

if rows <= 0 or columns <= 0:
    print("Rows and columns must be greater than 0.")

else:
    symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()