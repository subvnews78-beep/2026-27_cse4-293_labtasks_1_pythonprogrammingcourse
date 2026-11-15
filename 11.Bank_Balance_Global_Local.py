balance = 1000  # Global balance

def deposit(amount):
    global balance
    balance += amount
    print("Balance after deposit:", balance)

def show_local_balance():
    balance = 500  # Local variable
    print("Local balance:", balance)

deposit(500)

show_local_balance()

print("Actual Bank Balance:", balance)