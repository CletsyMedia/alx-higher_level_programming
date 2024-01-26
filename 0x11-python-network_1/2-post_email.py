#!/usr/bin/python3
"""
Module to send a POST request with email as a parameter
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print("Your email is: {}".format(body))
