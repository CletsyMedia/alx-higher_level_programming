#!/usr/bin/python3
"""
Module to fetch X-Request-Id value from the header of a URL response
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header_value = response.getheader('X-Request-Id')
        print(header_value)
