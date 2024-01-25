#!/bin/bash
# Sends a JSON POST request to a URL with the contents of a file in the body, and displays the body of the response.
json_file="$2"

if [ -f "$json_file" ]; then
    curl -sX POST -H "Content-Type: application/json" -d @"$json_file" "$1"
else
    echo "File not found or is not a regular file."
fi
