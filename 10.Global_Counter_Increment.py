counter = 0  # Global variable

def increment():
    global counter
    counter += 1

print("Before increment:", counter)

increment()

print("After increment:", counter)