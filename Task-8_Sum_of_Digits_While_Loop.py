# Sum of digits
number = int(input("Enter a number: "))
original_number = number
number = abs(number)
digit_sum = 0
while number > 0:
    digit = number % 10
    digit_sum += digit
    number //= 10
print(f"Sum of digits of {original_number} is {digit_sum}")
