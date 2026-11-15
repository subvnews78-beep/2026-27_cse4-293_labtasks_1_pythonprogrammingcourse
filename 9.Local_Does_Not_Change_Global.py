x = 10  # Global variable

def display():
    x = 20  # Local variable
    print("Inside function:", x)

display()

print("Outside function:", x)