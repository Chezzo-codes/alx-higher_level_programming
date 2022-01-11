#!/usr/bin/python3
"""
Script that sends a request to given url
displays the value of X-Request-Id variable
"""


if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as reply:
        print(reply.getheader('X-Request-Id'))
