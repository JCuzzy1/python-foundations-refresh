# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an
# appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        # convert input from a string to an integer
        inum = int(num) 
    except:
        print("Invalid input")
        continue
    
    # First number or new maximum
    if largest is None or inum > largest: 
        largest = inum

    # First number or new minimum
    if smallest is None or inum < smallest:
        smallest = inum

print("Maximum is", largest)
print("Minimum is", smallest)