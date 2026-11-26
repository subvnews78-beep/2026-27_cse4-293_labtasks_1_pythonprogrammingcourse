# Program to print a centered pyramid pattern of numbers
rows = int(input("Enter the number of rows: "))
for row_loop_var in range(1, rows + 1):

    for space_loop_var in range(1, rows - row_loop_var + 1):
        print(" ", end=" ")

    for number_loop_var in range(1, 2 * row_loop_var):
        print(number_loop_var, end=" ")

    print()