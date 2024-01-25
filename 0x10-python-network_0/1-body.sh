#!/bin/bash
# Takes a URL, sends a GET request using curl, and displays the body for a 200 status code.
response=$(curl -sL -w "%{http_code}" "$1" -o /dev/null); [ "$response" -eq 200 ] && curl -sL "$1"
