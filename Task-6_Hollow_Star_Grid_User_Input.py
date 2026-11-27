# Hollow star grid
rows = int(input("Enter grid size (rows and columns): "))
for row in range(1, rows + 1):
    for col in range(1, rows + 1):
        if row == 1 or row == rows or col == 1 or col == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
