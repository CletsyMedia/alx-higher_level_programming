#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    # Get the URL from the command-line argument
    url = sys.argv[1]

    try:
        # Try to open the URL and read the response
        with urllib.request.urlopen(url) as response:
            # Decode the response body in utf-8 and print it
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        # Handle HTTP errors by printing the error code
        print("Error code: {}".format(e.code))
