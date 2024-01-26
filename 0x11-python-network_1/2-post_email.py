#!/usr/bin/python3
"""
Module to display the value of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print("X-Request-Id:", x_request_id)
        print(response.read().decode('utf-8'))
