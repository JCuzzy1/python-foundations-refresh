# 8.5 Open the file mbox-short.txt and read it line by line. 
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. 
# Also look at the last line of the sample output to see how to print the count.

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt" # safe guard against user just pressing Enter rather than typing correct file name

count = 0
total = 0

fh = open(fname)
for line in fh:
    line = line.rstrip() # remove white space from end of line
    if not line.startswith('From ') : continue # if line doesn't start with From, skip to the top
    count = count + 1 # count = a running total

    words = line.split() # create list of words from the line
    email = words[1] # parse second word from the line, which is the email addresses
    print(email) # print list of email addresses

print("There were", count, "lines in the file with From as the first word")
