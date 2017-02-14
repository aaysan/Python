name = raw_input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)

email = dict()

for line in handle:
    if line.startswith("From"):
        word = line.split()
        email[word[1]] = email.get(word[1], 0) + 1

bigword = None
bigcount = None

for mail, count in email.items():
    if bigcount is None or count > bigcount:
        bigword = mail
        bigcount = count

print bigword, bigcount / 2
