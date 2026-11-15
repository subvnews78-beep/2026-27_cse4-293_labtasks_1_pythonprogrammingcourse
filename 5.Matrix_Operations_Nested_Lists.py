a = [[1, 2, 3],
     [4, 5, 6]]

b = [[7, 8, 9],
     [10, 11, 12]]

result = []

for i in range(len(a)):
    row = []
    for j in range(len(a[0])):
        row.append(a[i][j] + b[i][j])
    result.append(row)

print("First matrix:")
for row in a:
    print(row)

print("Second matrix:")
for row in b:
    print(row)

print("Sum of two matrices:")
for row in result:
    print(row)