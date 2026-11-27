# Star pyramid
rows = 3
for row in range(1, rows + 1):
    for col in range(rows - row):
        print("  ", end="")
    for col in range(2 * row - 1):
        print("*", end=" ")
    print()
