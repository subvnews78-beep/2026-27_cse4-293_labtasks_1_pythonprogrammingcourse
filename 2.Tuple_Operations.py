tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

# Concatenation
result = tuple1 + tuple2
print("Concatenated tuple:", result)

# Slicing
print("Sliced tuple:", result[1:4])

# Unpacking
a, b, c = tuple1

print("Unpacked values:")
print("a =", a)
print("b =", b)
print("c =", c)