def simple_interest(principal, time, rate=5):
    si = (principal * time * rate) / 100
    return si

# Calling with default rate
print("Simple Interest (Default Rate):", simple_interest(1000, 2))

# Calling with explicit rate
print("Simple Interest (Explicit Rate):", simple_interest(1000, 2, 10))