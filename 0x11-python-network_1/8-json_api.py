#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    # Set the default value for the letter
    q = "" if len(sys.argv) == 1 else sys.argv[1]

    # Make the POST request with the letter as a parameter
    response = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})

    try:
        # Try to parse the JSON response
        json_data = response.json()

        # Check if the JSON is not empty
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")

    except ValueError:
        # Handle invalid JSON
        print("Not a valid JSON")
