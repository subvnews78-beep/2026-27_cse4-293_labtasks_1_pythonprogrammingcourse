# Sum and average
total_input_numbers = int(input("Enter how many numbers: "))
if total_input_numbers <= 0:
    print("Enter a positive number of values")
else:
    total_sum = 0
    for i in range(total_input_numbers):
        number = float(input("Enter a number: "))
        total_sum += number
    average = total_sum / total_input_numbers
    print(f"Sum of {total_input_numbers} numbers is {total_sum:g}")
    print(f"Average of {total_input_numbers} numbers (sum {total_sum:g}) is {average:g}")
