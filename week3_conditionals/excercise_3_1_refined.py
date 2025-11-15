# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

h = float(hrs)
r = float(rate)

if h <= 40 :
    pay = h * r
else :
    ovh = h - 40    # overtime hours
    ovr = r * 1.5   # overtime rate
    pay = (40 * r) + (ovh * ovr)

# print("Pay: ", pay) # output to 2 decimal points

print(f"Pay: £{pay: .2f}")