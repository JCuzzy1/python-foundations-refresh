# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number
# print it out.
# X-DSPAM-Confidence:    0.8475

text = 'X-DSPAM-Confidence:    0.8475'
numstart = text.find('0')
numend = text.find('5')
# print(numstart) # 23
# print(numend) # 28

numtext = text[23:29]
fnumtext = float(numtext)
print(fnumtext) # 0.8475

