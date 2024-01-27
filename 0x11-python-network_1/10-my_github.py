#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys

if __name__ == "__main__":
    # Get username and password from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # URL for the GitHub API to get user information
    url = "https://api.github.com/user"

    # Make a GET request to the GitHub API with Basic Authentication
    response = requests.get(url, auth=(username, password))

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        user_data = response.json()

        # Display the user id
        print(user_data['id'])
    else:
        # Display None if the request was not successful
        print("None")
