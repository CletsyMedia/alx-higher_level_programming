#!/bin/bash
# Sends a GET request with a specific header using curl to the URL passed as the first argument and displays the body of the response.
curl -sH "X-School-User-Id: 98" "$1"
