# Program to print a diamond pattern of stars
rows = int(input("Enter the number of rows: "))
# Upper half of the diamond
for row_loop_var in range(1, rows + 1):

    for space_loop_var in range(1, rows - row_loop_var + 1):
        print(" ", end=" ")

    for star_loop_var in range(1, 2 * row_loop_var):
        print("*", end=" ")

    print()

# Lower half of the diamond
for row_loop_var in range(rows - 1, 0, -1):

    for space_loop_var in range(1, rows - row_loop_var + 1):
        print(" ", end=" ")

    for star_loop_var in range(1, 2 * row_loop_var):
        print("*", end=" ")

    print()