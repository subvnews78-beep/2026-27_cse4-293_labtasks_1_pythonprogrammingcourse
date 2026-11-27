# Diamond
rows = int(input("Enter number of rows (half diamond): "))
for row in list(range(1, rows + 1)) + list(range(rows - 1, 0, -1)):
    for col in range(rows - row):
        print("  ", end="")
    for col in range(2 * row - 1):
        print("*", end=" ")
    print()
