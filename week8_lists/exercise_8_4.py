# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list.
# and if not append it to the list.
# When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.

fname = input("Enter file name: ")
fh = open(fname)
lst = list() # empty list
for line in fh: # read file line by line
    line = line.rstrip() # remove white spcace at the end of line
    words = line.split() # split the line into list of words
    # print(words)
    for w in words: 
        if w not in lst: # for each word on each line check if word is already in the list
            lst.append(w) # if not append to the list

lst.sort()
print(lst)

# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 
# 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']