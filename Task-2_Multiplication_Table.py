# Multiplication table (for loop)
number = int(input("Enter a number: "))
for multiplier in range(1, 11):
    product = number * multiplier
    print(f"{number} x {multiplier} = {product}")
# Multiplication table (while loop)
number = int(input("Enter a number: "))
multiplier = 1
while multiplier <= 10:
    product = number * multiplier
    print(f"{number} x {multiplier} = {product}")
    multiplier += 1
