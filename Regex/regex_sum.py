import re

fp = raw_input("Enter the file:")

if len(fp) < 1:
    print "invalid input"
    quit()


handle = open(fp);

totalsum = 0 # the total sum


for line in handle:

    line = line.rstrip();
    res = re.findall('[0-9]+',line); #use regex to find all the numbers in a given file

    for num in res:
        totalsum = totalsum + int(num) #add them

print totalsum ##display
