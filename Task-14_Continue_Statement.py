# Continue (for loop)
n = int(input("Enter N (print 1 to N, skip even numbers): "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(f"Skipping even number {i} with continue (N is {n})")
        continue
    print(f"for loop odd number = {i} (up to {n})")

# Continue (while loop)
n = int(input("Enter N (print 1 to N, skip even numbers): "))
counter = 1
while counter <= n:
    if counter % 2 == 0:
        print(f"Skipping even number {counter} with continue (N is {n})")
        counter += 1
        continue
    print(f"while loop odd number = {counter} (up to {n})")
    counter += 1
