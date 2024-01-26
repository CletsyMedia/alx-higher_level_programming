#!/usr/bin/python3
"""
Module to send a POST request with email as a parameter
"""

import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    # Prepare the data
    email = argv[2]
    data = {"email": email}
    data = urllib.parse.urlencode(data).encode("ascii")

    # Create the request
    url = argv[1]
    req = urllib.request.Request(url, data)

    # Send the request and handle the response
    with urllib.request.urlopen(req) as response:
        # Retrieve X-Request-Id header
        x_request_id = response.headers.get('X-Request-Id')
        
        # Print the body of the response
        body = response.read()
        print(body.decode('utf-8'))

        # Optionally, print the X-Request-Id if available
        if x_request_id:
            print(f"X-Request-Id: {x_request_id}")
