#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    # Get the URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Define the payload with the email parameter
    payload = {'email': email}

    # Send a POST request to the URL with the payload
    response = requests.post(url, data=payload)

    # Display the body of the response
    print("Your email is: {}".format(response.text))
