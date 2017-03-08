import re

fp = raw_input("Enter the file:")

if len(fp) < 1:
    print "invalid input"
    quit()


handle = open(fp);

totalsum = 0
count = 0

for line in handle:

    line = line.rstrip();
    res = re.findall('[0-9]+',line);

    for num in res:
        count = count + 1
        totalsum = totalsum + int(num)

print totalsum
