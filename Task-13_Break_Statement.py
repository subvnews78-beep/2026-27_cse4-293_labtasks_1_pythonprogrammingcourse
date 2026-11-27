# Break (for loop)
n = int(input("Enter N (print until N, stop early at 5): "))
for i in range(1, n + 1):
    if i == 5:
        print(f"Breaking for loop at number {i} (N was {n})")
        break
    print(f"for loop number = {i} (up to {n})")

# Break (while loop)
n = int(input("Enter N (print until N, stop early at 5): "))
counter = 1
while counter <= n:
    if counter == 5:
        print(f"Breaking while loop at number {counter} (N was {n})")
        break
    print(f"while loop number = {counter} (up to {n})")
    counter += 1
