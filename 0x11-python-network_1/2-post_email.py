#!/usr/bin/python3
"""
Module to send a POST request with email as a parameter
"""

import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    value = {"email": email}
    data = urllib.parse.urlencode(value).encode("ascii")
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        body = response.read()
        print("Your email is: {}".format(body.decode('utf-8')))
