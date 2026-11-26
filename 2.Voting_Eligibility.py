# Read age from the user
age = int(input("Enter your age: "))
# Check voting eligibility
if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")