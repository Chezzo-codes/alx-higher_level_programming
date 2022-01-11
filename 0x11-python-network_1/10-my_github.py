#!/usr/bin/python3
"""
script takes githut creds and uses to display id
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    uid = requests.get('https://api.github.com/user',
                       auth=(argv[1], argv[2])).json()
    if "id" in uid:
        print(uid['id'])
    else:
        print(None)
