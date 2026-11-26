# Program to print a 5x5 hollow grid of stars
for row_loop_var in range(1, 6):
    for column_loop_var in range(1, 6):
        if row_loop_var == 1 or row_loop_var == 5 or column_loop_var == 1 or column_loop_var == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()