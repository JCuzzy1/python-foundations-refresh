# Write a function that:
# Ask the user for amount and rate
# Validate input with try/except
# Return the tax (amount * rate)
# Print the tax to 2 decimal places

def computetax(amount, rate):
    """Return the tax owed."""
    return amount * rate


# --- Main Program ---
try:
    amt = float(input("Enter amount: "))
    rt = float(input("Enter tax rate (e.g., 0.20 for 20%): "))
except:
    print("Error, please enter numeric input")
    quit()

tax = computetax(amt, rt)
print(f"Tax owed: £{tax:.2f}")


