import math

num = 0;

num = raw_input("Enter a number to check if its prime: ")
num = int(num)

if(num < 2):
    print num, "is not a prime number"
    quit()

i = 2
flag = 0

while (i <= math.sqrt(num)):
    if num % i == 0:
        print num, "is not a prime number"
        flag = 1
        break
    i = i + 1

if flag == 0:
    print num, "is a prime number"
