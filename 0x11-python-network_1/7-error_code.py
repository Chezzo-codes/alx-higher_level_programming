#!/usr/bin/python3
"""
script to send requests to url and display body of response
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    reply = requests.get(argv[1])
    code = reply.status_code
    if code > 400:
        print("Error code: {}".format(code))
    else:
        print(reply.text)
