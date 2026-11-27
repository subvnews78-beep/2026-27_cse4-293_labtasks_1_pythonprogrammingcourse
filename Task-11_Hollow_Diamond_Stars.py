# Hollow diamond
rows = 3
for row in list(range(1, rows + 1)) + list(range(rows - 1, 0, -1)):
    for col in range(rows - row):
        print("  ", end="")
    for col in range(1, 2 * row):
        if col == 1 or col == 2 * row - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
