#!/usr/bin/python3
"""
Python script that lists 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""

import requests
import sys

if __name__ == "__main__":
    # Get repository name and owner name from command line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # GitHub API endpoint for listing commits
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner_name, repo_name)

    try:
        # Make a GET request to the GitHub API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            commits = response.json()

            # Print the 10 most recent commits
            for i in range(10):
                sha = commits[i].get('sha')
                author_name = commits[i].get(
                    'commit').get('author').get('name')
                print('{}: {}'.format(sha, author_name))

        else:
            print('Error: Unable to fetch commits
                  (HTTP Status Code: {})'.format(response.status_code))

    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
