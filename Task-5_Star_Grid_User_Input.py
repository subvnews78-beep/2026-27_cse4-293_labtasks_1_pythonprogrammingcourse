# Filled star grid
rows = int(input("Enter grid size (rows and columns): "))
for row in range(1, rows + 1):
    for col in range(1, rows + 1):
        print("*", end=" ")
    print()
