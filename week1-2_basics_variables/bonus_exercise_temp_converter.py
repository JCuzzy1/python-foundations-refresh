# Get temperature in Celsius
celsius = input("Enter temperature in Celsius: ")
celsiusf = float(celsius)

# Convert to Fahrenheit
fahrenheit = (celsiusf * 9/5) + 32
fahrenheiti = int(fahrenheit) # Removes decimals like 68.0 → 68

# Show the result
print("Temperature in Fahrenheiti: ", fahrenheiti)