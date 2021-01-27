import random

a = random.randint(0,180)
print("The sine of {} is:".format(a))
a = (a/180)*3.14159265359
num = 3
factorial = 1
for e in range(1, num + 1):
    factorial = factorial*e
value = a - a**num/factorial

for i in range(2):
    num += 2
    factorial = 1
    for e in range(1, num + 1):
        factorial = factorial*e
    value += a**num/factorial
    num += 2 
    factorial = 1
    for e in range(1, num + 1):
        factorial = factorial*e
    value -= a**num/factorial

print(value)