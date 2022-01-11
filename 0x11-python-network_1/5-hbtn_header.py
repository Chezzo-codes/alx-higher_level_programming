#!/usr/bin/python3
"""
script that takes in a url to send a request to the url
and display the values of the variable X-Request-Id
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    reply = requests.get(argv[1])
    print(reply.headers.get('X-Request-Id'))
