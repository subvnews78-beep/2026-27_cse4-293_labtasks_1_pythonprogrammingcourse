# Reverse a number
number = int(input("Enter a number: "))
original_number = number
number = abs(number)
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
if original_number < 0:
    reversed_number = -reversed_number
print(f"Reverse of {original_number} is {reversed_number}")
