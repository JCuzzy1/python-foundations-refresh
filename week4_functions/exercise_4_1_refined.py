# Define function before calling it.
# Python allows calling later, but putting function definitions at the top is a common convention:

def computepay(h, r):
    # ---- Compute gross pay with overtime. ----
    if h <= 40:
        return h * r
    else:
        overtime_hours = h - 40
        overtime_rate = r * 1.5
        return (40 * r) + (overtime_hours * overtime_rate)


# ---- Main program ----

try:
    hrs = float(input("Enter Hours: ")) # float inputs more efficiently
    rate = float(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
    quit()

p = computepay(hrs, rate)
print(f"Pay: {p:.2f}") # rounds and displays two decimal places
