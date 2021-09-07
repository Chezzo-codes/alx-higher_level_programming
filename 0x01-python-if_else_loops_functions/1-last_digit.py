#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = str(number)[-1]
if int(last) > 5:
    if number < 0:
        print("Last digit of {} is -{} and is less than 6 and not 0".format(number, last))
    else:
        print("Last digit of {} is {} and is greater than 5".format(number, last))
elif int(last) == 0:
    print("Last digit of {} is {} and is 0".format(number, last))
elif int(last) < 6 and last != 0:
    if number < 0:
        print("Last digit of {} is -{} and is less than 6 and not 0".format(number, last))
    else:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, last))
