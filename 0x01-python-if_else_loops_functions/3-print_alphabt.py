#!/usr/bin/python3
letter = 97
while letter <= 122:
    print(chr(letter), end = '')
    letter += 1
    if letter == 101:
        letter += 1
    if letter == 113:
        letter += 1
