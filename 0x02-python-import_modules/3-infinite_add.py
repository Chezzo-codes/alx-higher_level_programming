#!/usr/bin/python3
import sys


def main(*argv):
    arglist = sys.argv
    arglen = len(arglist)
    result = 0

    if arglen > 1:
        for arg in arglist:
            if arg != arglist[0]:
                result += int(arg)
    print(result)

if __name__ == "__main__":
    main()
