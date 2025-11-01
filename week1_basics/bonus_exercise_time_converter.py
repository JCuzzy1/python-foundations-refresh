# Ask the user for total minutes
total_mins = input("Enter total minutes: ") # input produces a string
total_mins_int = int(total_mins) # convert string to a number (integer)

# Convert to hours and remaining minutes
hrs = total_mins_int // 60 # total mins divided by 60 gives hours. // removes decimals
mins = total_mins_int % 60 # gives me the remainder (minutes)

# Print the result
print(total_mins_int, "minutes is", hrs, "hour(s) and", mins, "minute(s). ")