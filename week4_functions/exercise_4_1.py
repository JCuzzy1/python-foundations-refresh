# Write a program to prompt the user for hours and rate per hour
# using input to compute gross pay.
# Pay should be the normal rate for hours up to 40 and
# time-and-a-half for the hourly rate for all hours worked above
# 40 hours.
# Put the logic to do the computation of pay in a function called
# computepay() and use the function to do the computation.
# The function should return a value. Use 45 hours and a rate of
# 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the
# string to a number.

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    h = float(hrs)
    r = float(rate)

except:
    print("Error, please enter numberic input")
    quit() # Exits program

def computepay(h, r) :
    if h <= 40 :
        pay = h * r
        return pay
    else :
        ovh = h - 40    # overtime hours
        ovr = r * 1.5   # overtime rate
        pay = (40 * r) + (ovh * ovr)
        return pay
    
p = computepay(h, r)
print("Pay: ", p) # output to 2 decimal points