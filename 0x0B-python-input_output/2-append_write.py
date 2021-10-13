#!/usr/bin/python3
"""
Module with funtion to append to a file
"""


def append_write(filename="", text=""):
"""
Returns file with apended text
"""
    with open(filename, 'a', "utf-8") as f:
        return f.write(str(text))
