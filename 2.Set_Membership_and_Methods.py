set_data = {10, 20, 30, 40}

print("Original set:", set_data)

# Membership testing
print("Is 20 present?", 20 in set_data)
print("Is 50 present?", 50 not in set_data)

# Add operation
set_data.add(50)
print("After add:", set_data)

# Remove operation
set_data.remove(30)
print("After remove:", set_data)

# Discard operation
set_data.discard(60)
print("After discard:", set_data)