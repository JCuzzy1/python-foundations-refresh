# Ask the user for hours and rate
hrs = input("Enter hours worked: ")
rate = input("Enter hourly rate: ")

# Convert to decimal numbers and Calculate pay
pay = float(hrs) * float(rate)

# Print the result
print("Pay: ", pay)

#Print the result to 2 decimal places
print(f"Pay: £{pay: .2f}")