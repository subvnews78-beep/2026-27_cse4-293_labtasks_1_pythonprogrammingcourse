number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
exponent = number1 ** number2

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")

if number2 != 0:
    division = number1 / number2
    floor_division = number1 // number2
    modulus = number1 % number2

    print(f"Division: {division}")
    print(f"Floor division: {floor_division}")
    print(f"Modulus: {modulus}")
else:
    print("Division, floor division and modulus are undefined for zero.")

print(f"Exponent: {exponent}")