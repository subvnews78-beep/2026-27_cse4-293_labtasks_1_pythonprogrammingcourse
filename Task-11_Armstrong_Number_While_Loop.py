# Armstrong number (3 digits)
number = int(input("Enter a 3-digit number: "))
original_number = number
armstrong_sum = 0
while number > 0:
    digit = number % 10
    armstrong_sum += digit ** 3
    number //= 10
if 100 <= original_number <= 999 and armstrong_sum == original_number:
    print(f"{original_number} is an Armstrong number (sum of cubes of digits is {armstrong_sum})")
else:
    print(f"{original_number} is not an Armstrong number (sum of cubes of digits is {armstrong_sum})")
