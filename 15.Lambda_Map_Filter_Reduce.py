from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using map()
squares = list(map(lambda x: x * x, numbers))

# Using filter()
even = list(filter(lambda x: x % 2 == 0, numbers))

# Using reduce()
total = reduce(lambda x, y: x + y, numbers)

print("Original List:", numbers)
print("Squares:", squares)
print("Even Numbers:", even)
print("Sum:", total)