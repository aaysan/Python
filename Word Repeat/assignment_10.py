name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

times = dict()
commons = list()

for line in handle:
    if line.startswith("From"):
        word = line.split()
        if len(word) > 2:
            temp = word[5].split(":")
            hour = temp[0]
            times[hour] = times.get(hour, 0) + 1


for hour, repeat in times.items():
    commons.append((hour, repeat))

commons.sort()

for hour, repeat in commons:
    print hour, repeat
