# Rewrite your pay program using try and except sp that your program handles non-numeric
# input gracefully by printing a message and exiting the program.

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    h = float(hrs)
    r = float(rate)

except:
    print("Error, please enter numberic input")
    quit() # Exits program 

if h <= 40 :
    pay = h * r
else :
    ovh = h - 40    # overtime hours
    ovr = r * 1.5   # overtime rate
    pay = (40 * r) + (ovh * ovr)

print("Pay: ", pay) # output to 2 decimal points