# Program to print an inverted right-angled triangle
rows = int(input("Enter the number of rows: "))
for row_loop_var in range(1, rows + 1):
    for column_loop_var in range(row_loop_var, rows + 1):
        print("*", end=" ")
    print()