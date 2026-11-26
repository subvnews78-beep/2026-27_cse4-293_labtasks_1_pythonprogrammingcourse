# Program to print a right-angled triangle using a user-defined symbol
rows = int(input("Enter the number of rows: "))
symbol = input("Enter the symbol to print: ")
for row_loop_var in range(1, rows + 1):
    for column_loop_var in range(1, row_loop_var + 1):
        print(symbol, end=" ")
    print()