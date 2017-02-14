import string
import random

def pass_generate(num):
    usables = string.printable

    if num <= 0:
        print 'Password needs to be at least 1 character.'
        quit()

    numbers = usables[:10]
    print numbers
    lower = usables[10:36]
    upper = usables[36:62]
    chars = usables[62:94]

    i = 0;

    password = list()

    while(i < num):
        password.append(usables[random.randint(0,94)])
        i = i + 1;

    if numbers not in password:
        password[num - 1] = usables[random.randint(0,10)]


    password = "".join(str(x) for x in password)

    print 'Your password is:', password



    return password

num = raw_input("Enter the length of the password: ")
try:
    num = int(num)
except:
    print 'You need to enter a valid number greater then zero.'
    quit()

password = pass_generate(num)
ans = raw_input("Would you like to save this password? (YES/NO) ")
if ans == 'YES':
    text_file = open("passwords.txt", "a")
    reason = raw_input("What is this password for? ")
    text_file.write('%s %s\n' %(reason, password))
    print 'Your password has been saved'
    text_file.close()
