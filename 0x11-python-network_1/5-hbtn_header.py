#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL,
and displays the value of the variable X-Request-Id in the response header
"""

import requests
import sys

if __name__ == "__main__":
    # Get the URL from command line argument
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Get the value of X-Request-Id from the response header
    x_request_id = response.headers.get('X-Request-Id')

    # Display the value of X-Request-Id
    print(x_request_id)
