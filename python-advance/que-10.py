#  10) Write a Python program to print custom exceptions.

bal = 1000
wb = 5000

if wb <= bal:
    print("Withdrawal successful")
    bal -= wb
    print(f"Remaining balance: {bal}")
else:
    raise ValueError("Insufficent balance")
assert:
wb <= bal, "Insufficent balance"