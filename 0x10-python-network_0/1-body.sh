#!/bin/bash
# Takes a URL, sends a GET request using curl, and displays the body for a 200 status code.
response=$(curl -sL -w "%{http_code}" "$1" -o /dev/null)
if [ "$response" -eq 200 ]; then curl -sL "$1"; fi
