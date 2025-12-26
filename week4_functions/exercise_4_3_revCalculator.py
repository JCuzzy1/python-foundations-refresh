# Write a function: def hours_needed(pay, rate):
# Given:
# Normal rate for 40 hours
# 1.5× overtime rate beyond 40
# Ask the user for a pay amount and a rate, then compute:
# “How many hours did the person work to earn that pay?”
# Return the number of hours.
# (You’re just reversing the logic of Exercise 4.6 — great brain workout.)

def hours_needed(pay, rate):
    """Return number of hours worked given pay and rate, using overtime after 40 hours."""
    a
    normal_pay = 40 * rate
    
    # Case 1: No overtime
    if pay <= normal_pay:
        return pay / rate
    
    # Case 2: Overtime involved
    overtime_pay = pay - normal_pay
    overtime_rate = rate * 1.5
    overtime_hours = overtime_pay / overtime_rate
    
    return 40 + overtime_hours


# --- Main Program ---

try:
    total_pay = float(input("Enter total pay: "))
    hourly_rate = float(input("Enter hourly rate: "))
except:
    print("Error, please enter numeric input")
    quit()

hours = hours_needed(total_pay, hourly_rate)
print(f"Hours worked: {hours:.2f}")