def calculate_marks(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return total, average

a = float(input("Enter marks of subject 1: "))
b = float(input("Enter marks of subject 2: "))
c = float(input("Enter marks of subject 3: "))

total, average = calculate_marks(a, b, c)

print("Total marks:", total)
print("Average marks:", average)