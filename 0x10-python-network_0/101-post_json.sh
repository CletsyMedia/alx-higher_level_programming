#!/bin/bash
# Sends a JSON POST request to a URL with the contents of a file in the body, and displays the body of the response.
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
