list_data = [10, 20, 30, 20, 40, 10, 50]
result = []
for item in list_data:
    if item not in result:
        result.append(item)
print("Original list:", list_data)
print("List after removing duplicates:", result)