#!/usr/bin/python3
"""
script that takes in url and sends a request to url
displays body of response
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from urllib.error import URLError, HTTPError
    from sys import argv
    rep = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(rep) as reply:
            print(reply.read().decode(encoding="utf-8"))
    except URLError as err:
        print("Error code: {}".format(err.code))
