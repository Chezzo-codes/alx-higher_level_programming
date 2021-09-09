#!/usr/bin/python3
import sys


def main(*argv):
    arglen = len(sys.argv) - 1
    arglist = sys.argv[1:]
    i = 1

    if arglen == 0:
        print("{} arguments.".format(arglen))
    elif arglen == 1:
        print("{} argument:".format(arglen))
    else:
        print("{} arguments:".format(arglen))

    for arg in arglist:
        print("{}: {}".format(i, arg))
        i += 1

if __name__ == "__main__":
    main()
